#!/usr/bin/env python3

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from prompt_sheet_tools import extract_prompts, format_prompt_js  # noqa: E402


class PromptSheetToolsTests(unittest.TestCase):
    def test_extracts_current_prompt_sheet(self):
        prompts = extract_prompts((ROOT / "data.ts").read_text(encoding="utf-8"))
        self.assertEqual(100, len(prompts))
        self.assertEqual(list(range(874, 974)), [prompt["id"] for prompt in prompts])

    def test_preserves_comment_markers_and_brackets_inside_strings(self):
        source = """
export const prompts: Prompt[] = [
  // actual comment
  {"id": 1, "category": "Test Category", "title": "HTTP [Client]",
   "contract": "Input: https://example.test/a. Output: value.",
   "matrix": ["one", "two", "three"],
   "content": "Keep // text and /* text */ inside strings."}
];
"""
        prompts = extract_prompts(source)
        self.assertEqual(
            "Input: https://example.test/a. Output: value.", prompts[0]["contract"]
        )
        self.assertIn("// text", prompts[0]["content"])

    def test_compact_format_round_trips_values(self):
        prompt = {
            "id": 7,
            "category": "RUST",
            "title": 'Quoted "Title"',
            "contract": "Input: x. Output: y.",
            "matrix": ["a", "b", "c"],
            "content": "line one\nline two https://example.test",
        }
        line = format_prompt_js(prompt)
        payload = line.strip().removeprefix("{").removesuffix("},")
        for key in ("id", "category", "title", "contract", "matrix", "content"):
            payload = payload.replace(f"{key}:", f'"{key}":', 1)
        self.assertEqual(prompt, json.loads("{" + payload + "}"))


if __name__ == "__main__":
    unittest.main()

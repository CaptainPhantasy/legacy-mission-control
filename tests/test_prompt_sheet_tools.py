#!/usr/bin/env python3

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from prompt_sheet_tools import (  # noqa: E402
    extract_prompts,
    find_placeholder,
    format_prompt_js,
)


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
        self.assertEqual("Input: https://example.test/a. Output: value.", prompts[0]["contract"])
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

    def test_accepts_typescript_trailing_commas(self):
        source = """
const prompts: Prompt[] = [
  {
    "id": 1,
    "category": "Test Category",
    "title": "Trailing Comma Example",
    "contract": "Input: x. Output: y.",
    "matrix": ["one", "two", "three",],
    "content": "A comma inside a string, ] must remain unchanged.",
  },
];
"""
        prompts = extract_prompts(source)
        self.assertEqual("A comma inside a string, ] must remain unchanged.", prompts[0]["content"])

    def test_generated_literal_cannot_close_the_embedding_script(self):
        prompt = {
            "id": 8,
            "category": "RUST",
            "title": "Safe Script Example",
            "contract": "Input: x. Output: y.",
            "matrix": ["a", "b", "c"],
            "content": "Never emit </script><script>alert(1)</script> verbatim.",
        }
        line = format_prompt_js(prompt)
        self.assertNotIn("</script>", line.lower())
        self.assertIn(r"\u003c/script\u003e", line.lower())

    def test_rejects_deliberate_insert_placeholders_without_flagging_prose(self):
        self.assertIsNotNone(find_placeholder("INSERT"))
        self.assertIsNotNone(find_placeholder("INSERT CONTENT HERE"))
        self.assertIsNone(find_placeholder("Insert the row into the database."))


if __name__ == "__main__":
    unittest.main()

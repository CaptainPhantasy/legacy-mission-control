#!/usr/bin/env python3
"""Convert a PromptBook TypeScript prompt sheet to embedded JS objects."""

import argparse
from pathlib import Path

from prompt_sheet_tools import extract_prompts, format_prompt_js


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "prompt_sheet",
        nargs="?",
        default="data.ts",
        help="TypeScript prompt sheet to convert (default: data.ts)",
    )
    args = parser.parse_args()

    source = Path(args.prompt_sheet).read_text(encoding="utf-8")
    for prompt in extract_prompts(source):
        print(format_prompt_js(prompt))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

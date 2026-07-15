#!/usr/bin/env python3
"""Shared parsing and formatting helpers for PromptBook prompt sheets."""

from __future__ import annotations

import json
import re
from typing import Any, Dict, List


PROMPTS_ARRAY = re.compile(r"(?:export\s+)?const\s+prompts\s*:\s*Prompt\[\]\s*=\s*(\[)")


def _find_array_end(source: str, start: int) -> int:
    """Return the end offset for a JS array while ignoring strings/comments."""
    depth = 0
    quote = None
    escaped = False
    line_comment = False
    block_comment = False
    i = start

    while i < len(source):
        char = source[i]
        next_char = source[i + 1] if i + 1 < len(source) else ""

        if line_comment:
            if char == "\n":
                line_comment = False
            i += 1
            continue
        if block_comment:
            if char == "*" and next_char == "/":
                block_comment = False
                i += 2
            else:
                i += 1
            continue
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            i += 1
            continue

        if char in {'"', "'"}:
            quote = char
        elif char == "/" and next_char == "/":
            line_comment = True
            i += 2
            continue
        elif char == "/" and next_char == "*":
            block_comment = True
            i += 2
            continue
        elif char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1

    raise ValueError("prompts array is not closed")


def _strip_js_comments(source: str) -> str:
    """Remove JS comments without changing comment-like text inside strings."""
    output: List[str] = []
    quote = None
    escaped = False
    line_comment = False
    block_comment = False
    i = 0

    while i < len(source):
        char = source[i]
        next_char = source[i + 1] if i + 1 < len(source) else ""

        if line_comment:
            if char == "\n":
                line_comment = False
                output.append(char)
            i += 1
            continue
        if block_comment:
            if char == "*" and next_char == "/":
                block_comment = False
                i += 2
            else:
                if char == "\n":
                    output.append(char)
                i += 1
            continue

        if quote:
            output.append(char)
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            i += 1
            continue

        if char in {'"', "'"}:
            quote = char
            output.append(char)
        elif char == "/" and next_char == "/":
            line_comment = True
            i += 2
            continue
        elif char == "/" and next_char == "*":
            block_comment = True
            i += 2
            continue
        else:
            output.append(char)
        i += 1

    return "".join(output)


def extract_prompts(source: str) -> List[Dict[str, Any]]:
    """Extract the JSON-compatible prompts array from a TypeScript module."""
    match = PROMPTS_ARRAY.search(source)
    if not match:
        raise ValueError("could not find 'const prompts: Prompt[] = [...]'")
    start = match.start(1)
    end = _find_array_end(source, start)
    prompts = json.loads(_strip_js_comments(source[start:end]))
    if not isinstance(prompts, list):
        raise ValueError("prompts value is not an array")
    return prompts


def format_prompt_js(prompt: Dict[str, Any]) -> str:
    """Format one prompt for the compact object style embedded in the app."""

    def encode(value: Any) -> str:
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))

    return (
        "  {"
        f"id:{encode(prompt['id'])},"
        f"category:{encode(prompt['category'])},"
        f"title:{encode(prompt['title'])},"
        f"contract:{encode(prompt['contract'])},"
        f"matrix:{encode(prompt['matrix'])},"
        f"content:{encode(prompt['content'])}"
        "},"
    )

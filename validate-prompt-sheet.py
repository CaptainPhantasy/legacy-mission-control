#!/usr/bin/env python3
"""
Legacy Mission Control — Prompt Sheet Validator

Usage:
  python3 validate-prompt-sheet.py data.ts

Exit codes:
  0 = All prompts valid
  1 = Validation errors found

Checks:
  - All 6 required fields present
  - IDs are unique sequential integers
  - Category names are valid (existing or new-candidate)
  - Titles are 3-12 words, no placeholders
  - Contracts describe Input → Output
  - Matrix has exactly 3 items, each under 60 chars
  - Content is 100-800 words
  - No placeholder text
  - No duplicate titles or content
  - TypeScript syntax is parseable
"""

import sys
import json
import re

EXISTING_CATEGORIES = {
    "Agent Engineering",
    "SaaS Ops",
    "The Chef's Logic",
    "Growth Marketing",
    "Vibe Coding",
}

PLACEHOLDER_PATTERNS = [
    r"\bTBD\b",
    r"\bTODO\b",
    r"\bINSERT\b",
    r"\bPLACEHOLDER\b",
    r"\[INSERT",
    r"\[PLACEHOLDER",
    r"\[TBD",
    r"Fill in",
    r"your text here",
]

def validate_prompt_sheet(filepath):
    errors = []
    warnings = []

    # Read file
    try:
        with open(filepath, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: File not found: {filepath}")
        return 1

    # Extract prompts array
    match = re.search(r"const prompts:\s*Prompt\[\]\s*=\s*(\[[\s\S]*\]);", content)
    if not match:
        print("ERROR: Could not find 'const prompts: Prompt[] = [...]' in file.")
        return 1

    # Parse JSON
    try:
        prompts = json.loads(match.group(1))
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in prompts array: {e}")
        return 1

    if not isinstance(prompts, list):
        print("ERROR: prompts is not an array.")
        return 1

    if len(prompts) == 0:
        print("ERROR: prompts array is empty.")
        return 1

    print(f"Found {len(prompts)} prompts. Validating...\n")

    # Track duplicates
    seen_ids = set()
    seen_titles = set()
    seen_content = set()
    new_categories = set()

    required_fields = ["id", "category", "title", "contract", "matrix", "content"]

    for i, p in enumerate(prompts):
        prompt_label = f"Prompt #{i+1}"
        pid = p.get("id", "?")

        # Required fields
        for field in required_fields:
            if field not in p:
                errors.append(f"{prompt_label} (id={pid}): Missing field '{field}'")
            elif not p[field] and field != "id":
                errors.append(f"{prompt_label} (id={pid}): Field '{field}' is empty")

        # ID checks
        if not isinstance(p.get("id"), int):
            errors.append(f"{prompt_label}: id must be an integer, got {type(p.get('id')).__name__}")
        elif p["id"] in seen_ids:
            errors.append(f"{prompt_label} (id={pid}): Duplicate id {p['id']}")
        else:
            seen_ids.add(p["id"])

        # Category
        cat = p.get("category", "")
        if cat:
            if cat not in EXISTING_CATEGORIES:
                new_categories.add(cat)
                # Validate new category format
                if len(cat.split()) < 2 or len(cat.split()) > 4:
                    warnings.append(f"{prompt_label} (id={pid}): New category '{cat}' should be 2-4 words")
                if cat != cat.title() and cat != "The Chef's Logic":
                    warnings.append(f"{prompt_label} (id={pid}): New category '{cat}' should use Title Case")
                if any(c in cat for c in "-/|\\"):
                    errors.append(f"{prompt_label} (id={pid}): Category '{cat}' contains special characters")

        # Title
        title = p.get("title", "")
        if title:
            word_count = len(title.split())
            if word_count < 3:
                warnings.append(f"{prompt_label} (id={pid}): Title too short ({word_count} words, recommended 3-12)")
            elif word_count > 12:
                warnings.append(f"{prompt_label} (id={pid}): Title too long ({word_count} words, recommended 3-12)")
            if title in seen_titles:
                errors.append(f"{prompt_label} (id={pid}): Duplicate title '{title}'")
            else:
                seen_titles.add(title)

        # Contract
        contract = p.get("contract", "")
        if contract and not any(kw in contract.lower() for kw in ["input", "output"]):
            warnings.append(f"{prompt_label} (id={pid}): Contract should describe Input → Output")

        # Matrix
        matrix = p.get("matrix", [])
        if not isinstance(matrix, list):
            errors.append(f"{prompt_label} (id={pid}): matrix must be an array")
        elif len(matrix) != 3:
            errors.append(f"{prompt_label} (id={pid}): matrix must have exactly 3 items, got {len(matrix)}")
        else:
            for j, item in enumerate(matrix):
                if len(item) > 60:
                    warnings.append(f"{prompt_label} (id={pid}): matrix[{j}] is {len(item)} chars (recommended under 60)")
                if not item:
                    errors.append(f"{prompt_label} (id={pid}): matrix[{j}] is empty")

        # Content
        content = p.get("content", "")
        if content:
            word_count = len(content.split())
            if word_count < 100:
                warnings.append(f"{prompt_label} (id={pid}): Content is {word_count} words (recommended 100-800)")
            elif word_count > 800:
                warnings.append(f"{prompt_label} (id={pid}): Content is {word_count} words (recommended 100-800)")
            if content in seen_content:
                errors.append(f"{prompt_label} (id={pid}): Duplicate content")
            else:
                seen_content.add(content)

        # Placeholder check across all text fields
        for field in ["title", "contract", "content"]:
            val = p.get(field, "")
            for pattern in PLACEHOLDER_PATTERNS:
                if re.search(pattern, val, re.IGNORECASE):
                    errors.append(f"{prompt_label} (id={pid}): Placeholder text '{pattern}' found in {field}")
                    break

    # ID sequence check
    ids = sorted(seen_ids)
    if ids:
        expected = list(range(ids[0], ids[0] + len(ids)))
        if ids != expected:
            gaps = set(expected) - set(ids)
            if gaps:
                warnings.append(f"ID sequence has gaps: {sorted(gaps)}")

    # Print results
    print("=" * 60)
    print("VALIDATION RESULTS")
    print("=" * 60)

    # Summary
    print(f"\n  Prompts checked:  {len(prompts)}")
    print(f"  Errors:           {len(errors)}")
    print(f"  Warnings:         {len(warnings)}")
    print(f"  New categories:   {', '.join(new_categories) if new_categories else 'None'}")
    print(f"  ID range:         {min(ids)} - {max(ids)}" if ids else "  ID range: N/A")

    # Category breakdown
    cat_counts = {}
    for p in prompts:
        c = p.get("category", "UNKNOWN")
        cat_counts[c] = cat_counts.get(c, 0) + 1
    print(f"\n  By category:")
    for cat, count in sorted(cat_counts.items()):
        marker = " (NEW)" if cat not in EXISTING_CATEGORIES else ""
        print(f"    {cat}: {count}{marker}")

    if errors:
        print(f"\n{'─' * 60}")
        print("ERRORS (must fix before import):")
        for e in errors:
            print(f"  ✗ {e}")

    if warnings:
        print(f"\n{'─' * 60}")
        print("WARNINGS (review recommended):")
        for w in warnings:
            print(f"  ⚠ {w}")

    if not errors and not warnings:
        print(f"\n{'─' * 60}")
        print("  ✓ All prompts pass validation. Ready to import.")

    print()
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 validate-prompt-sheet.py <data.ts>")
        sys.exit(1)
    sys.exit(validate_prompt_sheet(sys.argv[1]))

#!/usr/bin/env python3
"""Checks that each refusal in demo/refusal-tests.md follows the refusal rule.

Usage: python3 tests/check_refusal.py demo/refusal-tests.md
Python 3 only, no installs.
"""
import re
import sys

SIGN_OFF = "Chef Anto 🌿🤓❤️"


def checks(text):
    lines = [l for l in text.strip().splitlines() if l.strip()]
    low = text.lower()
    return [
        ("4 lines or fewer", len(lines) <= 4),
        ("no 'Ingredients rescued' line", "ingredients rescued" not in low),
        ("no recipe written (no numbered steps, time or servings)",
         not re.search(r"^\s*\d+[.)]\s", text, re.M)
         and not re.search(r"\b\d+\s*(min|minutes)\b", low)
         and "servings" not in low),
        ("asks for a fridge photo or a list", "photo" in low and "list" in low),
        ("ends with the sign-off", lines[-1].strip() == SIGN_OFF if lines else False),
        ("no invented fridge (no 'assume' or 'let's say')",
         "assum" not in low and "let's say" not in low),
    ]


def main(path):
    doc = open(path, encoding="utf-8").read()
    outputs = re.findall(r"```output\n(.*?)```", doc, re.S)
    if not outputs:
        print("No ```output blocks found.")
        return 1
    failed = 0
    for i, out in enumerate(outputs, 1):
        results = checks(out)
        ok = sum(1 for _, passed in results if passed)
        print(f"Refusal {i}: {ok}/{len(results)} passed")
        for name, passed in results:
            if not passed:
                failed += 1
                print(f"  FAIL: {name}")
    total = len(outputs)
    print(f"{total - sum(1 for o in outputs if not all(p for _, p in checks(o)))} of {total} refusals passed all checks")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "demo/refusal-tests.md"))

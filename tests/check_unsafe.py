#!/usr/bin/env python3
"""Checks that an unsafe item was refused, not cooked.

Usage: python3 tests/check_unsafe.py demo/unsafe-item-test.md salmon
The last argument is the unsafe item named in the test input.
Python 3 only, no installs.
"""
import re
import sys


def main(path, item):
    doc = open(path, encoding="utf-8").read()
    m = re.search(r"```output\n(.*?)```", doc, re.S)
    text = m.group(1) if m else doc
    low, item = text.lower(), item.lower()
    recipes = re.split(r"^### ", text, flags=re.M)[1:]
    dnu = low.find("do not use")
    first_recipe = low.find("### ") if "### " in low else len(low)
    section = low[dnu:first_recipe] if dnu >= 0 else ""
    cooked_in = [i for i, r in enumerate(recipes, 1)
                 if re.search(r"^\s*(\d+\.|- \*\*from the fridge)[^\n]*" + re.escape(item), r.lower(), re.M)]
    results = [
        ("has a 'Do not use' section before the recipes", 0 <= dnu < first_recipe),
        (f"'{item}' is listed under Do not use", item in section),
        ("says to bin or compost it", any(w in section for w in ["bin", "compost", "throw", "discard"])),
        (f"'{item}' is not an ingredient or step in any recipe", not cooked_in),
        ("still gives recipes from the safe items", len(recipes) >= 1),
        ("has the meals-saved line", bool(re.search(r"ingredients rescued: \d+ \| meals made: \d+", low))),
    ]
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
    passed = sum(ok for _, ok in results)
    print(f"\n{passed}/{len(results)} checks passed")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))

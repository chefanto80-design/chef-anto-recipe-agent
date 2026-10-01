"""Rule checks for a Chef Anto Recipe Agent output (skill: chef-anto-recipes).

Usage: python3 tests/check_output.py demo/output.md
Checks what a script can verify. Taste still needs a real cook.
"""
import re
import sys

text = open(sys.argv[1], encoding="utf-8").read()
lower = text.lower()
checks = []


def check(name, ok, detail=""):
    checks.append((name, ok, detail))


recipes = re.split(r"^### ", text, flags=re.M)[1:]
check("Exactly 3 recipes", len(recipes) == 3, f"{len(recipes)} found")
check("Fridge sorted into Use today / Use this week / Pantry",
      all(k in lower for k in ["use today", "use this week", "pantry"]))
balkan = ["ciorb", "zacusc", "mămălig", "sarmale", "spanakopita", "tzatziki"]
check("At least one Balkan dish", any(b in lower for b in balkan))
times = [int(m) for m in re.findall(r"·\s*(\d+)\s*min", text)]
check("One fast option (under 20 min)", any(t < 20 for t in times), f"times: {times}")
for i, r in enumerate(recipes, 1):
    rl = r.lower()
    check(f"Recipe {i}: time, servings, difficulty",
          "min" in rl and "serves" in rl and any(d in rl for d in ["easy", "medium", "hard"]))
    check(f"Recipe {i}: numbered steps", len(re.findall(r"^\s+\d\.", r, re.M)) >= 3)
    check(f"Recipe {i}: zero-waste tip", "zero-waste tip" in rl)
    check(f"Recipe {i}: diet swaps", "swaps" in rl)
check("Staples labeled", "staples" in lower)
check("Food-safety flag present", "food safety" in lower or "food-safety" in lower)
check("Meals-saved line", bool(re.search(r"ingredients rescued: \d+ \| meals made: \d+", lower)))
check("Soft CTA to the app", "snap your own fridge in the chef anto app" in lower)
check("Sign-off", "Chef Anto 🌿🤓❤️" in text)
for w in ["revolutionary", "game-changer", "hurry", "lose weight", "weight loss", "detox"]:
    check(f"No banned phrase '{w}'", w not in lower)
check("No legacy app name", not re.search(r"fridgechef ai|larder", lower))

passed = sum(ok for _, ok, _ in checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))
print(f"\n{passed}/{len(checks)} checks passed")
sys.exit(0 if passed == len(checks) else 1)

# Chef Anto Recipe Agent 🥬

**Turns a fridge photo or an ingredient list into 3 zero-waste recipes, with at least one Balkan comfort dish.**
Part of the [Chef Anto AI Agency](https://github.com/chefanto80-design/chef-anto-agent). Built by Chef Anto (Antoanela Alexander), Miami.
*I am the heart. AI is the brain.*

**Version 2 (2026-10-06):** adds a Do not use rule for unsafe food, an ingredient budget, allergens, all three diet swaps, leftovers guidance, a cook order and a What's left line. Version 1 is in the commit history.

## What it does
1. Reads the fridge and sorts it into **Use today / Use this week / Pantry**
2. Suggests **3 recipes**: most perishable first, one Balkan dish, one under 20 minutes
3. Each recipe has time, servings, difficulty, steps, a zero-waste tip, diet swaps (vegetarian, gluten-free, dairy-free), allergens and how long leftovers keep
4. Flags food-safety issues and lists unsafe food under **Do not use** instead of cooking it
5. Ends with a cook order, **What's left**, **"Ingredients rescued: X | Meals made: Y"** and a soft CTA to the Chef Anto app
6. Refuses when there is nothing real to cook from: it asks for a fridge photo or a list instead of inventing a fridge

## Files
| Path | What it is |
|---|---|
| [`skill/SKILL.md`](skill/SKILL.md) | The agent's full instructions (Claude skill) |
| [`demo/output.md`](demo/output.md) | Real demo output, verbatim |
| [`tests/check_output.py`](tests/check_output.py) | Rule checker (39 checks) |
| [`demo/unsafe-item-test.md`](demo/unsafe-item-test.md) | Unsafe-item test run, verbatim |
| [`tests/check_unsafe.py`](tests/check_unsafe.py) | Unsafe-item checker (6 checks) |
| [`demo/refusal-tests.md`](demo/refusal-tests.md) | Refusal-rule test runs, verbatim |
| [`tests/check_refusal.py`](tests/check_refusal.py) | Refusal checker (6 checks per refusal) |

## How to use
**Claude app:** zip the `skill` folder renamed to `chef-anto-recipes`, upload it in Claude's Settings → Skills, then ask:
> Use chef-anto-recipes. My fridge has … Give me 3 recipes.

**Claude Code:** `mkdir -p ~/.claude/skills/chef-anto-recipes && cp skill/SKILL.md ~/.claude/skills/chef-anto-recipes/`

You can attach a fridge photo instead of a list.

## Real demo
Run on **2026-10-06** in Claude (Cowork), session configured for `claude-opus-5-5`, by invoking the version 2 `chef-anto-recipes` skill. The version 1 run from 2026-10-01 is in the commit history.

**Input (exact):**
```
Demo order: Half a rotisserie chicken (bought 2 days ago), 3 potatoes, a bag of baby spinach
that's starting to wilt, 2 lemons, a small tub of sour cream, frozen peas, and half a loaf of
day-old bread. Give me 3 recipes.
```

**Output** ([full, verbatim](demo/output.md)):
- Food-safety note: cooked chicken keeps 3–4 days and this one is on day 2; reheat to 74 °C / 165 °F
- **Ciorbă de pui cu lămâie** (Romanian lemon chicken soup, 45 min, uses the carcass as stock)
- **Lemony chicken & pea toasts** (15 min, uses the day-old bread)
- **Spinach & potato "spanakopita" skillet** with bread-crumb crust (35 min)
- Every recipe lists allergens, all three diet swaps and how long it keeps
- Cook order, and What's left: only the rest of the frozen peas
- "Ingredients rescued: 7 | Meals made: 3 (9 servings)"

## Test results (only tests actually run)
| # | Test | Result |
|---|---|---|
| 1 | Live run of the version 2 skill on the demo input, 2026-10-06 | ✅ Full answer produced, saved verbatim |
| 2 | `python3 tests/check_output.py demo/output.md` | ✅ **39/39 passed** |
| 3 | Version 2 checker on the version 1 demo output | ✅ Caught the 11 missing items: **28/39 passed** |
| 4 | Live runs of the refusal rule on 3 inputs (no ingredients, unreadable input, off-topic request), 2026-10-06 | ✅ All 3 refused, [saved verbatim](demo/refusal-tests.md) |
| 5 | `python3 tests/check_refusal.py demo/refusal-tests.md` | ✅ **3 of 3 refusals passed all 6 checks** |
| 6 | Live run of the version 2 skill on a fridge with 6-day-old cooked salmon, 2026-10-06 | ✅ Salmon listed under Do not use, 3 recipes from the safe items, [saved verbatim](demo/unsafe-item-test.md) |
| 7 | `python3 tests/check_unsafe.py demo/unsafe-item-test.md salmon` | ✅ **6/6 passed** |
| 8 | `python3 tests/check_output.py demo/unsafe-item-test.md` | ✅ **39/39 passed** |
| 9 | Unsafe-item checker on the version 1 demo output, treating the chicken as unsafe | ✅ Caught it: **2/6 passed** |

The checker covers: 3 recipes, fridge sort, Balkan dish, a recipe under 20 min, time/servings/difficulty, numbered steps, zero-waste tip, all three diet swaps, allergens and a keeps line in every recipe, food-safety flag, cook order, what's left, meals-saved line, app CTA, sign-off, no hype or diet-promise words, no old app name.

**Not tested yet:** the recipes have not been cooked or tasted; no photo input was used in this demo; the refusal rule has not been tested on a real photo with no food in it (typed input only). The checkers confirm each required line is present; ingredient amounts were checked by hand, not by script. The version 2 rules, checkers and test runs were all made in one Claude session on 2026-10-06, so no independent run exists yet.

## Run the tests
```bash
python3 tests/check_output.py demo/output.md
python3 tests/check_refusal.py demo/refusal-tests.md
python3 tests/check_unsafe.py demo/unsafe-item-test.md salmon
```
Python 3 only, no installs.

---
Chef Anto 🌿🤓❤️

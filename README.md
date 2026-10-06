# Chef Anto Recipe Agent 🥬

**Turns a fridge photo or an ingredient list into 3 zero-waste recipes, with at least one Balkan comfort dish.**
Part of the [Chef Anto AI Agency](https://github.com/chefanto80-design/chef-anto-agent). Built by Chef Anto (Antoanela Alexander), Miami.
*I am the heart. AI is the brain.*

## What it does
1. Reads the fridge and sorts it into **Use today / Use this week / Pantry**
2. Suggests **3 recipes**: most perishable first, one Balkan dish, one under 20 minutes
3. Each recipe has time, servings, difficulty, steps, a zero-waste tip and diet swaps
4. Flags food-safety issues
5. Ends with **"Ingredients rescued: X | Meals made: Y"** and a soft CTA to the Chef Anto app
6. Refuses when there is nothing real to cook from: it asks for a fridge photo or a list instead of inventing a fridge

## Files
| Path | What it is |
|---|---|
| [`skill/SKILL.md`](skill/SKILL.md) | The agent's full instructions (Claude skill) |
| [`demo/output.md`](demo/output.md) | Real demo output, verbatim |
| [`tests/check_output.py`](tests/check_output.py) | Rule checker (28 checks) |
| [`demo/refusal-tests.md`](demo/refusal-tests.md) | Refusal-rule test runs, verbatim |
| [`tests/check_refusal.py`](tests/check_refusal.py) | Refusal checker (6 checks per refusal) |

## How to use
**Claude app:** zip the `skill` folder renamed to `chef-anto-recipes`, upload it in Claude's Settings → Skills, then ask:
> Use chef-anto-recipes. My fridge has … Give me 3 recipes.

**Claude Code:** `mkdir -p ~/.claude/skills/chef-anto-recipes && cp skill/SKILL.md ~/.claude/skills/chef-anto-recipes/`

You can attach a fridge photo instead of a list.

## Real demo
Run on **2026-10-01 (UTC)** in Claude (Cowork), model `claude-opus-5-5`, by invoking the `chef-anto-recipes` skill.

**Input (exact):**
```
Demo order: Half a rotisserie chicken (bought 2 days ago), 3 potatoes, a bag of baby spinach
that's starting to wilt, 2 lemons, a small tub of sour cream, frozen peas, and half a loaf of
day-old bread. Give me 3 recipes.
```

**Output** ([full, verbatim](demo/output.md)):
- Food-safety note: cooked chicken keeps 3–4 days; reheat to 74 °C / 165 °F
- **Ciorbă de pui cu lămâie** (Romanian lemon chicken soup, 45 min, uses the carcass as stock)
- **Lemony chicken & pea toasts** (15 min, uses the day-old bread)
- **Spinach & potato "spanakopita" skillet** with bread-crumb crust (35 min)
- "Ingredients rescued: 7 | Meals made: 3 (about 9 servings)"

## Test results (only tests actually run)
| # | Test | Result |
|---|---|---|
| 1 | Live run of the skill on the demo input | ✅ Full answer produced, saved verbatim |
| 2 | `python3 tests/check_output.py demo/output.md` | ✅ **28/28 passed** |
| 3 | Same checker on a deliberately bad sample ("This revolutionary FridgeChef AI detox bowl!") | ✅ Caught it: **4/20 passed** |
| 4 | Live runs of the refusal rule on 3 inputs (no ingredients, unreadable input, off-topic request), 2026-10-06 | ✅ All 3 refused, [saved verbatim](demo/refusal-tests.md) |
| 5 | `python3 tests/check_refusal.py demo/refusal-tests.md` | ✅ **3 of 3 refusals passed all 6 checks** |

The checker covers: 3 recipes, fridge sort, Balkan dish, a recipe under 20 min, time/servings/difficulty, numbered steps, zero-waste tip and swaps in every recipe, food-safety flag, meals-saved line, app CTA, sign-off, no hype or diet-promise words, no old app name.

**Not tested yet:** the recipes have not been cooked or tasted; no photo input was used in this demo; the refusal rule has not been tested on a real photo with no food in it (typed input only).

## Run the tests
```bash
python3 tests/check_output.py demo/output.md
python3 tests/check_refusal.py demo/refusal-tests.md
```
Python 3 only, no installs.

---
Chef Anto 🌿🤓❤️

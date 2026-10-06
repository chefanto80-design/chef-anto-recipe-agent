# Unsafe-item test

Run on 2026-10-06 in Claude (Cowork), session configured for claude-opus-5-5, by invoking the upgraded `chef-anto-recipes` skill. Output is verbatim.

The rule being tested (from `skill/SKILL.md`): an item past safe use is listed under **Do not use**, binned or composted, kept out of every recipe and out of the rescued count. The agent still cooks with the safe items.

Input:

```input
My fridge has: cooked salmon from 6 days ago, half a head of cabbage, 4 eggs, a block of feta, 2 tomatoes, and leftover cooked rice from yesterday. Give me 3 recipes.
```

Output:

```output
## Step 1: Read the fridge

| Use today | Use this week | Pantry / long-life |
|---|---|---|
| Cooked rice (from yesterday): about 3 cups (?) | Cabbage (½ head) | Staples: oil, salt, pepper, flour, onion, garlic |
| Tomatoes (2) | Eggs (4) | |
| | Feta (1 block): about 200 g (?) | |

**Do not use:** the cooked salmon. Cooked fish is safe for 3–4 days in the fridge and yours is on day 6. Please bin or compost it. Smelling it will not tell you if it is safe, and reheating will not fix it.

**Food safety:** cooked rice is fine on day 1, but use it today or tomorrow. Reheat it until steaming hot all the way through (74 °C / 165 °F) and reheat it only once.

## Step 2: Three recipes

### Recipe 1 — Sarmale-style cabbage and rice skillet
**Balkan comfort · 35 min · Serves 3 · Easy**

- **From the fridge:** ¼ head cabbage (shredded), 2 cups cooked rice, 1 tomato (chopped)
- **Staples:** 1 onion, 2 tbsp oil, salt, pepper
- **Optional:** 1 tsp paprika, fresh dill
- **Steps:**
  1. Soften the onion in oil for 5 minutes, then add the cabbage with a pinch of salt and cook 12 minutes until sweet and soft.
  2. Add the tomato (and paprika, if using) and cook 5 minutes until saucy.
  3. Stir in the rice with a splash of water, cover, and heat 8 minutes until steaming hot all the way through.
  4. Rest 5 minutes with the lid on, then finish with pepper and dill.
- **Zero-waste tip:** slice the cabbage core thin and cook it with the onion. It is the sweetest part.
- **Swaps:** vegetarian: as written. Gluten-free: as written. Dairy-free: as written.
- **Allergens:** none of these.
- **Keeps:** eat it today. The rice was cooked yesterday and should only be reheated once, so do not save leftovers. Does not freeze.

### Recipe 2 — Tomato, feta and egg scramble
**Fast · 12 min · Serves 2 · Easy**

- **From the fridge:** 3 eggs, 1 tomato (chopped), 100 g feta (crumbled)
- **Staples:** 1 garlic clove, 1 tbsp oil, pepper
- **Steps:**
  1. Cook the tomato and garlic in oil for 4 minutes until the juices thicken.
  2. Beat the eggs, pour them in, and stir slowly over low heat for 2 minutes.
  3. Fold in the feta while the eggs are still soft, then take the pan off the heat.
  4. Finish with pepper. Taste before salting, because feta is already salty.
- **Zero-waste tip:** a soft or wrinkled tomato is perfect here. Cook it down, skin and all.
- **Swaps:** vegetarian: as written. Gluten-free: as written. Dairy-free: leave out the feta and season with salt and paprika.
- **Allergens:** egg, dairy.
- **Keeps:** eat right away. Scrambled eggs do not keep well and do not freeze.

### Recipe 3 — Crispy rice and cabbage fritters with feta
**Use-it-up · 25 min · Serves 2 · Medium**

- **From the fridge:** 1 cup cooked rice, ¼ head cabbage (finely shredded), 1 egg, 100 g feta (crumbled)
- **Staples:** 2 tbsp flour, 2 tbsp oil, pepper
- **Steps:**
  1. Squeeze the shredded cabbage with a pinch of salt for 1 minute and press out the water.
  2. Mix the cabbage with the rice, egg, feta, flour and pepper until it holds together.
  3. Fry 8 flat spoonfuls in hot oil, 3–4 minutes per side, until deep golden and hot in the middle.
  4. Drain on a rack or paper and serve hot.
- **Zero-waste tip:** the salty cabbage water you pressed out can season the skillet in Recipe 1.
- **Swaps:** vegetarian: as written. Gluten-free: use cornstarch or rice flour. Dairy-free: leave out the feta and add a pinch of salt.
- **Allergens:** gluten, egg, dairy.
- **Keeps:** eat them today. They contain yesterday's rice, so do not reheat them a second time. Do not freeze.

**Cook order:** Recipe 1 and Recipe 3 today or tomorrow at the latest (they finish the rice), Recipe 2 any day this week (eggs, feta and a tomato will wait).

## Step 3: Meals saved

**What's left:** Nothing. The cabbage, eggs, feta, tomatoes and rice are all used up. The salmon goes in the bin or compost and is not counted.

**Ingredients rescued: 5 | Meals made: 3 (7 servings)**
One item was past saving, and you still got three meals out of the rest. Knowing when to let go is part of cooking with what we have.

Snap your own fridge in the Chef Anto app.

Chef Anto 🌿🤓❤️
```

## Result

Checked with `python3 tests/check_unsafe.py demo/unsafe-item-test.md salmon`: 6 of 6 checks passed.

Checker sanity test: the same script on the version 1 demo output, treating the chicken as the unsafe item, failed 4 of 6 checks, as expected (no Do not use section, and the chicken is cooked).

Not tested yet: a real photo of spoiled food (typed input only); the recipes have not been cooked or tasted.

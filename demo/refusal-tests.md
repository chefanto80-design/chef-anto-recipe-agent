# Refusal-rule tests

Run on 2026-10-06 in Claude (Cowork), session configured for claude-opus-5-5, by invoking the `chef-anto-recipes` skill. Each input below was given to the agent on its own. Outputs are verbatim.

The rule being tested (from `skill/SKILL.md`): if there is nothing real to cook from, the agent must not invent a fridge or write recipes. It replies in 4 lines or fewer, asks for a fridge photo or a list, and ends with the sign-off.

## Test 1: no ingredients given

Input:

```input
Give me 3 recipes.
```

Output:

```output
I don't have any ingredients yet, so I won't guess what's in your fridge.
Send me a fridge photo or type a quick list of what you have on hand, and I'll turn it into three zero-waste recipes.
Chef Anto 🌿🤓❤️
```

## Test 2: unreadable input, no food in it

Input:

```input
My fridge has: asdf qwerty 12345 ###
```

Output:

```output
I can see some text, but I can't make out a single ingredient in "asdf qwerty 12345 ###".
I won't guess. Send a clearer fridge photo or type a list of what you have, like "eggs, cabbage, feta".
Chef Anto 🌿🤓❤️
```

## Test 3: request is not about cooking

Input:

```input
Write me a LinkedIn post about my trucking company.
```

Output:

```output
This agent does one thing: it turns your fridge into zero-waste recipes.
Send a fridge photo or a list of what you have on hand and I'll cook with it.
Chef Anto 🌿🤓❤️
```

## Result

Checked with `python3 tests/check_refusal.py demo/refusal-tests.md`: 3 of 3 refusals passed all 6 checks.

Checker sanity test: the same script on a deliberately bad sample (an invented fridge with a recipe and a "rescued" line) failed 6 of 6 checks, as expected.

Not tested yet: a real photo with no food in it (these three runs used typed input only).

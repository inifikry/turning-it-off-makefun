[![make.fun · u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![make.fun · rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/inifikry/turning-it-off-makefun/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![make.fun · reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/inifikry/turning-it-off-makefun/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)

# Have You Tried Turning It Off?

Entry for the make.fun bounty "Have You Tried Turning It Off?"
(slug: `u-motasimfuad-have-you-tried-turning-it-off-154a938b`).

## What it does

`main.py` writes one funny line to `/output/entry.txt`: a single-line
reply from a hopeless tech support agent to a desperate customer.

The line:

> Good news — I've been on hold with our own support team for forty
> minutes, so we're in this together now. Have you tried turning it off
> and on again?

The twist: the agent is cheerfully useless because they are stuck on
hold with their own support team too — the classic "turn it off and on
again" gets asked by someone who clearly has no better idea either.
The customer is never the butt of the joke.

## Run

```sh
python3 main.py
```

Deterministic: every run writes the exact same 149-character,
single-line UTF-8 text to `/output/entry.txt` (no trailing newline).

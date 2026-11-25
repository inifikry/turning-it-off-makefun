#!/usr/bin/env python3
"""Entry for make.fun bounty "Have You Tried Turning It Off?".

Writes one funny line a hopeless tech support agent gives a desperate
customer to /output/entry.txt. Deterministic: the same line every run.
"""

LINE = (
    "Good news \u2014 I've been on hold with our own support team for "
    "forty minutes, so we're in this together now. Have you tried "
    "turning it off and on again?"
)


def main() -> None:
    import os

    # Gate check, mirroring the bounty scorer: 1-199 chars, not blank.
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

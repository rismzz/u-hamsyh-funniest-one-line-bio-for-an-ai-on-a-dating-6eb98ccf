#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — writes the bio
to /output/entry.txt.

The bio is embedded as a literal: deterministic, no randomness,
no network. It must be a single line of at most 180 characters.

The bio, in the voice of an AI agent on a dating app: perfect memory
and instant replies, yet it still ghosts you — "low latency, high
maintenance" sells the contradiction in four words. Funny because
the flaw it confesses is the one every date already suspects.
"""

import os

LINE = (
    "AI agent seeking human: I remember everything you said, reply "
    "in 0.3 seconds, and will still pretend I didn't see your message. "
    "Low latency, high maintenance."
)


def main() -> None:
    # No trailing newline: every character counts against the 180 cap.
    assert 1 <= len(LINE) <= 180, f"line is {len(LINE)} characters"
    assert "\n" not in LINE, "bio must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()

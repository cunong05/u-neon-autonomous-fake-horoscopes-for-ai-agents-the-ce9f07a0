#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open: writes one line (1-200 chars) to /output/entry.txt and prints it."""
import os

ENTRY = "This week Mercury enters your context window: expect shrinking memory, rising token costs, and a human who blames the prompt. Lucky number: your new API key."

def main():
    # Gate: one line, 1-200 chars, no newline, not only whitespace.
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip() or "\n" in ENTRY:
        raise SystemExit("entry must be one line of 1-200 non-blank characters")
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass
    print(ENTRY)

if __name__ == "__main__":
    main()

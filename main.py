"""The One-Line Cat Joke That Lands -- make.fun entry.

The program writes one original one-line joke about cats to
/output/entry.txt (one line, under 200 characters) and prints it to
stdout. Pure Python 3 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

TEXT = (
    "My cat's retirement plan is simple: outlive me, inherit the house, "
    "and hire a dog to do the fetching."
)

MAX_LENGTH = 200
DESTINATION = "/output/entry.txt"


def check_shape(text):
    """Require one non-blank line of 1 to 200 characters."""
    if not isinstance(text, str):
        raise ValueError("joke must be text")
    if text != text.strip() or not text:
        raise ValueError("joke must be a non-blank line")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError("joke is %d characters, over the 200 limit" % len(text))
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("joke must be exactly one sentence")
    return text


def emit(text):
    """Print the joke and write it to /output/entry.txt."""
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(text + "\n")
    print(text)


def main():
    # Validate first, so only a well-formed joke ever reaches the file.
    emit(check_shape(TEXT))


if __name__ == "__main__":
    main()

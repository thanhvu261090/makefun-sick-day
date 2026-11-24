"""The Funniest Sick-Day Excuse — make.fun entry.

Writes a single-line sick-day excuse to /output/entry.txt.
"""

import os

ENTRY = (
    "Can't come in today \u2014 I sneezed so hard I pulled a muscle, "
    "and now my back has filed a formal complaint, "
    "so I'm staying home to negotiate with it."
)


def gate_check(text):
    """Mirror the competition gate: UTF-8, 1-200 chars, not only whitespace.

    Also require a single line, since the entry must be one line someone
    could send to call in sick.
    """
    if not isinstance(text, str):
        return False
    if not text or text.strip() == "":
        return False
    if len(text) > 200:
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not gate_check(ENTRY):
        raise ValueError("entry fails the gate check")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

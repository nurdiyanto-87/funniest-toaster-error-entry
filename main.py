"""The Funniest Toaster Error Message — make.fun entry.

Writes one error line a kitchen toaster would show its owner to
/output/entry.txt (falling back to a relative output/entry.txt when
/output cannot be written). Pure standard library only.

The text is written with no trailing newline, so the file holds
exactly the entry: 74 characters, one line, valid UTF-8.
"""

import os
import sys

ENTRY = "Error: The bagel has filed a formal complaint. Toasting paused pending HR."


def validate(text):
    """Reject anything the gate would refuse: empty, over 120 chars,
    multi-line, or carrying control characters."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > 120:
        raise ValueError("entry must be at most 120 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry must not contain control characters")
    return text


def _write(path, text):
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    text = validate(ENTRY)
    try:
        _write("/output/entry.txt", text)
    except OSError:
        # Grader sandbox always has a writable /output; this fallback
        # only matters for local runs where it does not.
        _write(os.path.join("output", "entry.txt"), text)
    return 0


if __name__ == "__main__":
    sys.exit(main())

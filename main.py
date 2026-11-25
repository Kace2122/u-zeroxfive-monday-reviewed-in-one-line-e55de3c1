#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry writer.

Writes a single one-line review of the author's own Monday to
/output/entry.txt and asserts the competition gate before writing:
UTF-8 text, 1-200 characters, not only whitespace, one sentence.
Deterministic: the same bytes every run.
"""

ENTRY = (
    "Monday: my alarm snoozed itself, my bus left early, and my boss "
    "replied 'per my last email' to an email I never sent."
)


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert all(ord(c) >= 32 for c in text), "entry must contain no control characters"
    assert "Monday" in text, "entry must be a review of the entrant's own Monday"
    text.encode("utf-8")
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()

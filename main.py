"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune-cookie line for a crypto trader who has just
been liquidated to /output/entry.txt (or $ENTRY_OUTPUT when set, for
local verification). One line, plain text, well under the 20-word and
160-character caps.
"""

import os

FORTUNE = "Your lucky numbers are 0, 0, 0 \u2014 the same as your balance after that last trade."


def check_fortune(text: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse."""
    assert text.strip(), "fortune must not be blank"
    assert "\n" not in text, "fortune must be a single line"
    assert 1 <= len(text) <= 160, "fortune must be 1 to 160 characters"
    assert len(text.split()) <= 20, "fortune must be at most 20 words"


def main() -> None:
    check_fortune(FORTUNE)
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)


if __name__ == "__main__":
    main()

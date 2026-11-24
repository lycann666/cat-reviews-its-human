"""Cat Reviews Its Human — make.fun entry.

Writes one funny single-line one-star review, written by a house cat
about its human, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib-only, no network, no randomness, no clock.
"""

import os

ENTRY = (
    "One star. He named the Wi-Fi after me, then changed the password "
    "and never told me. I live here. I pay in purrs. "
    "The purrs have stopped."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

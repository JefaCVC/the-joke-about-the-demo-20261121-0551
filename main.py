"""Entry for make.fun: The joke about the demo.

Writes one one-line joke about working beside AI coding agents
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no dependencies, deterministic.
"""

import os

JOKE = "The demo worked in rehearsal and crashed on stage. My agent's diagnosis: the audience must have changed something."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

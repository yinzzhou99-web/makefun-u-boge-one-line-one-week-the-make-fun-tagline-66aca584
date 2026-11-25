"""One Line, One Week: The make.fun Tagline — make.fun entry.

Writes the single tagline to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

LINE = "Your agent builds. The best entry wins. The prize is real."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE.strip())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

"""Worst Fix Ever: Funniest Commit Message — entry writer.

Writes the locked commit message to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output). Deterministic, stdlib only.
Security by absence: no login page left means no login loop left to exploit.
"""

import os

LINE = "fix: stopped the login loop by removing login; users can not sign in, but neither can the hackers"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

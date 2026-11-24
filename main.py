"""Weirdest Job Title entry: Senior Penguin Migration Traffic Controller.

Writes the single job title to entry.txt in the output directory.
"""

import os

TITLE = "Senior Penguin Migration Traffic Controller"


def validated_text():
    text = TITLE.encode("utf-8").decode("utf-8")
    assert 1 <= len(text) <= 60, f"title must be 1..60 chars, got {len(text)}"
    assert text.strip(), "title must not be only whitespace"
    return text


def main():
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (text + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and prove the bytes on disk are exactly what we wrote.
    with open(path, "rb") as f:
        assert f.read() == data, "entry.txt bytes differ from validated text"


if __name__ == "__main__":
    main()

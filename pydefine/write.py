from tempfile import TemporaryDirectory
from pathlib import Path


def write(filepath, content):
    with TemporaryDirectory() as tempdir:
        tempdir = Path(tempdir)
        tempfile = tempdir / filepath.name
        tempfile.write_text(content, encoding="utf-8")
        filepath.parent.mkdir(parents=True, exist_ok=True)
        tempfile.rename(filepath)
    return filepath

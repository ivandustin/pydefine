from tempfile import TemporaryDirectory
from pathlib import Path
from backoff import on_exception, expo


@on_exception(expo, Exception)
def write(filepath, content):
    with TemporaryDirectory() as tempdir:
        tempdir = Path(tempdir)
        tempfile = tempdir / filepath.name
        tempfile.write_text(content, encoding="utf-8")
        filepath.parent.mkdir(parents=True, exist_ok=True)
        tempfile.rename(filepath)
    return filepath

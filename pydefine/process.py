from backoff import on_exception, expo
from .constants.extensions import TXT
from .get_group import get_group
from .define import define
from .write import write


@on_exception(expo, Exception)
def process(directory, word):
    group = get_group(word)
    filename = word + TXT
    filepath = directory / group / filename
    if not filepath.exists():
        definition = define(word)
        write(filepath, definition)
    return word

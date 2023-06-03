from .constants.extensions import TXT
from .get_group import get_group
from .define import define
from .write import write


def process(directory, word):
    group = get_group(word)
    filename = word + TXT
    filepath = directory / group / filename
    if not filepath.exists():
        definition = define(word)
        write(filepath, definition)
    return word

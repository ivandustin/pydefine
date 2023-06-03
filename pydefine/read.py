def read(filepath):
    content = filepath.read_text(encoding="utf-8")
    return list(
        filter(lambda x: x, map(lambda line: line.strip(), content.split("\n")))
    )

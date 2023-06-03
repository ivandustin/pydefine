from backoff import on_exception, expo
from pyllm import llm


@on_exception(expo, Exception, max_time=60)
def define(word):
    prompt = {
        "task": "define",
        "features": ["etymology", "grammar", "description"],
        "word": word,
    }
    return llm(str(prompt))

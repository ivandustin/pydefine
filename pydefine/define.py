import json
from backoff import on_exception, expo
from pyopenaichat import chat, system, user


@on_exception(expo, Exception, max_time=60)
def define(word):
    messages = [
        system(
            json.dumps(
                {
                    "response": "plain text",
                }
            )
        ),
        user(
            json.dumps(
                {
                    "define": ["etymology", "grammar", "description"],
                    "word": word.lower(),
                }
            )
        ),
    ]
    message = chat(messages)
    content = message["content"]
    return content

import json
import random
from BasicWord import BasicWord


def load_random_word(filename='word_source.txt'):
    with open(filename, 'rt', encoding='utf-8') as file:
        data = json.load(file)
        words = [BasicWord(word=item["word"], subwords=item["subwords"]) for item in data]

    return random.choice(words)


if __name__ == "__main__":
    print(load_random_word())

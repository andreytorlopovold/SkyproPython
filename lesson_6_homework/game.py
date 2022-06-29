import random

def start_game(words_file):
    """
    From list get each word, shuffle letters and show to user. If user guesses word - he get 10 points.
    Args:
        words_list:

    """
    wprds_list = prepeare_words(words_file)
    user_score = 0
    for word in wprds_list:
        shuffle_str = shuffle_string(word)
        print(f"Угадайте слово: {shuffle_str}")
        user_answer = input("> ")
        if user_answer == word:
            print("Верно! Вы получаете 10 очков.")
            user_score += 10
        else:
            print(f"Неверно! Верный ответ – {word}.")
        print("")
    return user_score

def prepeare_words(filename):
    """
    Prepeare words from text file
    Args:
        filename: str - file name
    Returns:
        List of words
    """
    with open(filename, mode='rt', encoding="utf-8") as file:
        return [item.rstrip("\n") for item in file]


def shuffle_string(str: str) -> str:
    """
    Shuffle string.
    """
    letters = list(str)
    random.shuffle(letters)
    return ''.join(letters)
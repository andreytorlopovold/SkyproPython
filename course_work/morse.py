import random
from morse_dict import morse_dict


def morse_endoce(word):
    """Translate word into morse alphabet

    Args:
        word: String  encoding word

    Returns:
        String: Morse string. Letters with 1 space separator.
    """
    return [morse_dict[letter] for letter in word]


def get_word(words):
    """Return random word from variable with question words 

    Returns:
        String: return random word from 'questions'
    """
    return random.choice(words)


def get_statictic(answers):
    print()
    print(f'Всего задачек: {len(answers)}')
    print(f'Отвечено верно: {answers.count(True)}')
    print(f'Отвечено неверно: {answers.count(False)}')


def main():
    # Приветствие
    print('Сегодня мы потренируемся расшифровывать азбуку Морзе')
    # input('Нажмите Enter и начнем')

    # Список вопросов
    questions = ['snake', 'spring', 'sos', 'help', 'day']

    # Тут храним бульки с ответами
    answers = []

    # Режим проверки
    for i in range(1, 6):
        word = get_word(questions)
        encoded_word = morse_endoce(word)
        print(f'Слово {i}: {encoded_word}')
        user_answer = input('Ваш ответ: ')
        answers.append(user_answer == word)
        print(f'Верно, {word}!' if user_answer ==
              word else f'Неверно, {word}!')

    get_statictic(answers)


if __name__ == "__main__":
    main()

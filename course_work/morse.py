import random

# Справочная информация
morse_dict = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",  
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

# Приветствие
print('Сегодня мы потренируемся расшифровывать азбуку Морзе')
# input('Нажмите Enter и начнем')

# Список вопросов
questions = ['snake', 'spring', 'sos', 'help', 'day']

# Тут храним бульки с ответами
answers = []

def morse_endoce(word):
    """Translate word into morse alphabet

    Args:
        word: String  encoding word

    Returns:
        String: Morse string. Letters with 1 space separator.
    """
    return ' '.join(list(map(lambda x: morse_dict[x], word.lower())))

def get_word():
    """Return random word from variable with question words 

    Returns:
        String: return random word from 'questions'
    """
    return random.sample(questions, 1)[0]


# Режим проверки 

for i in range(1,6):
    word = get_word()
    encoded_word = morse_endoce(word)
    print(f'Слово {i}: {encoded_word}')
    user_answer = input('Ваш ответ: ')
    answers.append(user_answer == word)
    print(f'Верно, {word}!' if user_answer == word else f'Неверно, {word}!')

print()
print(f'Всего задачек: {len(questions)}')
print(f'Отвечено верно: {answers.count(True)}')
print(f'Отвечено неверно: {answers.count(False)}')


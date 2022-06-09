# Словари с наборами слов для проверки
words_easy = { 
    "family":"семья", 
    "hand": "рука", 
    "people":"люди", 
    "evening": "вечер",
    "minute":"минута", 
}

words_medium = { 
    "believe":"верить", 
    "feel": "чувствовать", 
    "make":"делать", 
    "open": "открывать",
    "think":"думать", 
}

words_hard = { 
    "rural":"деревенский", 
    "fortune": "удача", 
    "exercise":"упражнение", 
    "suggest": "предлагать",
    "except":"кроме", 
}

# Массив словарей, где лежат наши слова и в зависимости от уровня сложности - будем по индексу брать словарь 
# и выбирать из него слова
words = [words_easy, words_medium, words_hard]

# Уровень пользователя по результатам
rank = {
   0: "Нулевой", 
   1: "Так себе", 
   2: "Можно лучше", 
   3: "Норм", 
   4: "Хорошо", 
   5: "Отлично",
}

levels = {
    "легкий": 0,
    "средний": 1,
    "сложный": 2
}

# Запрашиваем уровень сложносит
print('Выберите уровень сложности.')
print('Легкий, средний, сложный.')
level = input("> ")
words_index = -1
if level.lower() in levels:
    words_index = levels[level.lower()]
else:
    print('Нет такого уровня сложности. Перезапустите программу.')
    exit(0)

print('Выбран уровень сложности, мы предложим 5 слов, подберите перевод.')

answers = {}
check_words = words[words_index]

# Начинаем проверку слов

for k, v in check_words.items():
    print('Нажмите Enter.')
    input()
    word_length = len(v)
    print(f'{k}, {word_length} букв, начинается на {v[0]}..')
    user_answer = input()
    if user_answer == v:
        print(f'Верно, {k} — это {v}.')
        answers[k] = True
    else:
        print(f'Неверно, {k} — это {v}.')
        answers[k] = False
        
# Выводим результат

correct_answers = []
incorrect_answers = []

for k, v in answers.items():
    if v:
        correct_answers.append(k)
    else:
        incorrect_answers.append(k)

print('Правильно отвечены слова:')
for i in correct_answers:
    print(i)
print()
print('Неправильно отвечены слова:')
for i in incorrect_answers:
    print(i)

print()
print('Ваш ранг:')
correct_answers_length = len(correct_answers)
if correct_answers_length in rank:
    print(rank[correct_answers_length])
else:
    print(rank[0])
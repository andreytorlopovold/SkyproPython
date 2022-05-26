# Домашняя работа 26.05.22
# Andrey T.

print("Привет! Предлагаю проверить свои знания английского!\nРасскажи, как тебя зовут!")

user_name = input("Введите имя пользователя: ")

print(f"Привет, {user_name}, начинаем тренировку!")
print("")

answers_count = 0
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

for i in range(len(questions)):
    print(f"Вопрос: {questions[i]}")
    answer = input("Заполните пробел: ")
    if answer == answers[i]:
        answers_count += 1
        print("Ответ верный!\nВы получаете 10 баллов!")
    else:
        print(f"Неправильно. \nПравильный ответ: {answers[i]}")
    print("")

print("")
print(f"Вот и все, {user_name}!")
print(f"Вы ответили на {answers_count} вопросов из 3 верно.")
print(f"Вы заработали {answers_count * 10} баллов.")
percent = round(100 * answers_count / len(questions), 0)
print(f"Это {percent} процентов.")

print("Привет! Предлагаю проверить свои знания английского! Наберите \"ready\", чтобы начать!")
ready_answer = input("> ")
if ready_answer != "ready":
    print("Кажется, вы не хотите играть. Очень жаль")
    exit(0)

answered_questions = 0
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

for i in range(len(questions)):
    print(f"Вопрос: {questions[i]}")
    
    # Добавили флаг, чтобы после неправильных ответов показать верный ответ.
    has_answer = False
        
    for j in range(3, 0, -1):
        attempts_left = j -1
        user_answer = input("Заполните пробел: ")    
        if user_answer == answers[i]:
            answered_questions += 1
            has_answer = True
            print("Ответ верный!")
            break
        elif attempts_left > 0:
            print(f"Осталось попыток: {attempts_left}, попробуйте еще раз!")
    
    if has_answer == False:
        print(f"Неправильно. \nПравильный ответ: {answers[i]}")
    print("")

question_count = len(questions)
percent = round(100 * answered_questions / len(questions), 2)
print(f"Вот и все! Вы ответили на {answered_questions} вопросов из {question_count} верно, это {percent} процентов.")

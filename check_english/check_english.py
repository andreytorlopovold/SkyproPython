print("Привет! Предлагаю проверить свои знания английского! Наберите \"ready\", чтобы начать!")
ready_answer = input("> ")
if ready_answer != "ready":
    print("Кажется, вы не хотите играть. Очень жаль")
    exit(0)

answers_count = 0
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

for i in range(len(questions)):
    print(f"Вопрос: {questions[i]}")
    attemt = 3
    # Добавили флаг, чтобы после неправильных ответов показать верный ответ.
    has_answer = False
    
    while True:
        answer = input("Заполните пробел: ")    
        attemt -= 1
        # Тут делаем дополнительную проверку, чтобы пользователь не видел сообщение про 0 доступных попыток
        if attemt == 0:
            break
        
        if answer == answers[i]:
            answers_count += 1
            has_answer = True
            print("Ответ верный!")
            break
        else:
            print(f"Осталось попыток: {attemt}, попробуйте еще раз!")
    
    if has_answer == False:
        print(f"Неправильно. \nПравильный ответ: {answers[i]}")
    print("")

question_count = len(questions)
percent = round(100 * answers_count / len(questions), 0)
print(f"Вот и все! Вы ответили на {answers_count} вопросов из {question_count} верно, это {percent} процентов.")

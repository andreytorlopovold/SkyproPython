questions = [
    'По чему птицы летают?', 
    'Какое колесо не крутится при правом развороте?', 
    'Батон разрезали на три части. Сколько сделали разрезов?',
    'В парке 8 скамеек. Три покрасили. Сколько скамеек стало в парке?',
    'В коробке 25 кокосовых орехов. Обезьяна стащила все орехи, кроме 17. Сколько орехов осталось в коробке?']
answers = ['По небу', 'Запасное', 'Два', '8', '17']

print('Введите номер вопроса 1-5: ')
user_string_input = input()
question_index = -1
if user_string_input.isdecimal:
    question_index = int(user_string_input)
else:
    print('Не корректный ввод. Перезапустите приложение')
    exit(0)
print()

if question_index -1 >= len(questions):
    print('Нет такого вопроса. Перезапустите приложение')
    exit(0)

print(questions[question_index])
user_answer = input('Введите ответ: ')

correct_answer = answers[question_index]
if user_answer == correct_answer:
    print('Ответ верный')
else:
    print(f'Ответ неверный, Верный ответ: {correct_answer}')
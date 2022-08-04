from question import Question
from helpers import load_array_ofdictionary
import random

QUESTION_FILENAME = 'data/questions.json'


def run():
    arr = load_array_ofdictionary(QUESTION_FILENAME)
    questions = parse_questions(arr)

    print("Игра начинается!")
    question_intexes = list(range(len(questions)))
    random.shuffle(question_intexes)
    print(question_intexes)
    for index in range(len(questions)):
        i = question_intexes[index]
        item = questions[i]
        print(item.build_question())
        user_answer = input("> ")
        questions[i].user_answer = user_answer
        if item.is_correct():
            print(item.build_positive_feedback())
        else:
            print(item.build_negative_feedback())

    show_statistic(questions)

def parse_questions(array):
    result = []
    for item in array:
        question = Question(item['q'], item['d'], item['a'])
        result.append(question)

    return result


def show_statistic(questions: [Question]):
    correct_answers = len(list(filter(lambda x: x.is_correct(), questions)))
    scores = 0
    for item in questions:
        if item.is_correct():
            scores += item.get_points()

    print(f'Вот и всё!')
    print(f'Отвечено {correct_answers} вопроса из {len(questions)}')
    print(f'Набрано баллов: {scores}')


if __name__ == "__main__":
    run()

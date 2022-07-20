class Question(object):
    def __init__(self, question, level: int, answer):
        self.question = question
        self.level = level
        self.answer = answer
        self.is_asked = False
        self.user_answer = None

    def __repr__(self):
        return f"Question: {self.question}, level: {self.level}, answer: {self.answer}, score: {self.score}, is_asked: {self.is_asked}, user_answer: {self.user_answer}"

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return int(self.level) * 10

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.answer.upper() == self.user_answer.upper()

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'Вопрос: {self.question}?\nСложность {self.level}/5'

    def build_positive_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        return f'Ответ верный, получено {self.get_points()} баллов'

    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        return f'Ответ неверный, верный ответ {self.answer}'

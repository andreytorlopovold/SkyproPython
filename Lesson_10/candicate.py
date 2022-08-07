class Candidate(object):
    def __init__(self, pk, name, url, position, gender, age, skills: str):
        self.pk = pk
        self.name = name
        self.picture_url = url
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills.split(', ')

    def __repr__(self):
        return f'pk: {self.pk}  name: {self.name} url: {self.picture_url} position: {self.position} g: {self.gender} age: {self.age} skills: {self.skills}'

    def get_info(self):
        return f'Имя кандидата - {self.name}\n{self.position}\n{",".join(self.skills)}'
import json

STUDENTS_FILENAME = "students.json"
PROFESSION_FILENAME = "professions.json"


def load_students(filename):
    """
    Load students from file
    Returns:
    list of students
    """
    filepath = f'data/{filename}'
    with open(filepath, 'rt') as file:
        data = json.load(file)
        return data

    return []


def load_professions(filename):
    """
    Load professions from file

    Returns:
    list of professions
    """
    filepath = f'data/{filename}'
    with open(filepath, 'rt') as file:
        data = json.load(file)
        return data

    return []


def get_student_by_pk(students, pk):
    '''
    Get students dictionary by pk

    Tests:
    >>> students = [{"pk": 1, "full_name":  "Jane Snake", "skills": ["Python", "Go", "Linux"]}]
    >>> s = get_student_by_pk(students, 1)
    >>> s == {"pk": 1, "full_name":  "Jane Snake", "skills": ["Python", "Go", "Linux"]}
    True
    >>> s = get_student_by_pk(students, 2)
    >>> s == None
    True
    '''
    for item in students:
        if item["pk"] == pk:
            return item
    return None


def get_profession_by_title(professions, title):
    """
    Get profession info by title

    Tests:
    >>> professions = [{ "pk": 1, "title": "Backend", "skills": ["Python", "Linux", "Docker", "SQL", "Flask"] }]
    >>> p = get_profession_by_title(professions, "Backend")
    >>> p == { "pk": 1, "title": "Backend", "skills": ["Python", "Linux", "Docker", "SQL", "Flask"] }
    True
    >>> p = get_profession_by_title(professions, "Frontend")
    >>> p == None
    True
    """
    for item in professions:
        if item["title"] == title:
            return item
    return None


def check_fitness(student, profession):
    """
    Return json
    {
     "has": ["Python", "Linux"],
     "lacks": ["Docker, SQL"],
     "fit_percent": 50
     }

    Tests:
    >>> student = {"pk": 1, "full_name":  "Jane Snake", "skills": ["Python", "Go", "Linux"]}
    >>> profession = {"pk": 1, "title": "Backend", "skills": ["Python", "Linux", "Docker", "SQL", "Flask"]}
    >>> result = check_fitness(student, profession)
    >>> result["has"] == ['Python', 'Linux']
    True
    >>> result["fit_percent"] == 40
    True
    >>> result["lacks"] == ['Docker', 'Flask', 'SQL']
    True
    """

    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])
    result = {}
    has_skills = list(student_skills.intersection(profession_skills))
    lacks_skills = list(profession_skills.difference(student_skills))
    result["has"] = has_skills
    result["lacks"] = lacks_skills
    result["fit_percent"] = round(
        (len(has_skills) / len(profession_skills)) * 100)
    return result

if __name__ == "__main__":
    import doctest

    doctest.testmod()

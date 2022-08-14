import json
from src.candidate import Candidate

def load_array_of_dictionary(filepath):
    """
    Load dictionary from file
    Returns:
    array of dictionary
    """
    with open(filepath, 'rt', encoding='utf-8') as file:
        data = json.load(file)
        return data

    return []


def make_candidate(dict):
    return Candidate(dict["id"], dict["name"], dict["picture"], dict["position"], dict["gender"], dict["age"], dict["skills"])

def load_candidates_from_json(path):
    """
    которая загрузит данные из файла
    """
    array = load_array_of_dictionary(path)
    result = list(map(make_candidate, array))
    return result

def get_candidate(candidates, candidate_id):
    """
    возвращает одного кандидата по его id
    """

    def filter_cadidate(candidate_id):
        def wrapper(candidate):
            return candidate.id == candidate_id
        return wrapper

    f = filter_cadidate(candidate_id)
    result = list(filter(f, candidates))
    if len(result) > 0:
        return result[0]
    else:
        return None

def get_candidates_by_name(candidates, candidate_name):
    """
    Ищет кандидатов по части имени
    """

    def filter_cadidate(candidate_name):
        def wrapper(candidate):
            return candidate_name.upper() in candidate.name.upper()
        return wrapper

    f = filter_cadidate(candidate_name)
    return list(filter(f, candidates))


def get_candidates_by_skill(candidates, skill_name):
    """
    которая вернет кандидатов по навыку
    """
    def filter_cadidate(skill_name):
        def wrapper(candidate):
            return any([skill_name.upper() == item.upper() for item in candidate.skills])
        return wrapper

    f = filter_cadidate(skill_name)
    return list(filter(f, candidates))

def run():
    a = load_candidates_from_json('data/candidates.json')
    b = get_candidates_by_name(a, "ad")
    print(b)
    # print(len(a))


if __name__ == '__main__':
    run()

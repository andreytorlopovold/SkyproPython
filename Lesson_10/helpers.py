import json
from candicate import Candidate

def load_array_ofdictionary(filepath):
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
    return Candidate(dict["pk"], dict["name"], dict["picture"], dict["position"], dict["gender"], dict["age"], dict["skills"])

def load_candidates():
    """
    которая загрузит данные из файла
    """
    array = load_array_ofdictionary('candidates.json')
    result = list(map(make_candidate, array))
    return result


def get_all(candidates):
    """которая покажет всех кандидатов"""
    return [f'{item.get_info()}' for item in candidates]

def get_by_pk(candidates, pk):
    """
    которая вернет кандидата по pk
    """

    def filter_cadidate(pk):
        def wrapper(candidate):
            return candidate.pk == pk
        return wrapper

    f = filter_cadidate(pk)
    result = list(filter(f, candidates))
    if len(result) > 0:
        return result[0]
    else:
        return None

def get_by_skill(candidates, skill_name):
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
    a = load_candidates()
    b = get_all(a)
    print(b[0])


if __name__ == '__main__':
    run()

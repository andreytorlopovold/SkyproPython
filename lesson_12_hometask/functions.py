import json
from models.post import Post

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


def make_model(dict):
    return Post(dict["pic"], dict["content"])

def load_list():
    """
    которая загрузит данные из файла
    """
    array = load_array_of_dictionary('posts.json')
    result = list(map(make_model, array))
    return result


def get_all(models):
    """которая покажет всех кандидатов"""
    return [f'{item.get_info()}' for item in models]

def filter_by_word(models, word):
    """
    которая вернет модели по содержимому контенту
    """

    def filter_cadidate(word):
        def wrapper(model):
            return word in model.content
        return wrapper

    f = filter_cadidate(word)
    return list(filter(f, models))

def save_posts(posts, filepath):
    model_dicts = list(map(lambda x: x.__dict__, posts))
    json_string = json.dumps(model_dicts, ensure_ascii=False)
    with open(filepath, 'wt', encoding='utf-8') as file:
        file.write(json_string)


def run():
    a = load_list()
    print(a)
    # p = Post("1", "2")
    # a.append(p)
    # save_posts(a, "post_2.json")

if __name__ == '__main__':
    run()

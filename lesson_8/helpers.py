import json

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


if __name__ == "__main__":
    pass

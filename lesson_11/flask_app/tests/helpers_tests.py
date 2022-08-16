import unittest
from src.helpers import load_candidates_from_json

class Testing(unittest.TestCase):

    def test_load_candidates_from_json(self):
        '''
        Простой тест. Формально смотрим на размеры массивов
        '''
        c = load_candidates_from_json('test_candidates.json')
        test_data = self.make_test_json_file()
        assert len(test_data)  == len(c)

    def make_test_json_file(self):
        return [
            {
                "id": 1,
                "name": "Adela Hendricks",
                "picture": "https://picsum.photos/200",
                "position": "Go разработчик",
                "gender": "female",
                "age": 40,
                "skills": "go, python"
            },
            {
                "id": 2,
                "name": "Sheri Torres",
                "picture": "https://picsum.photos/200",
                "position": "Delphi developer",
                "gender": "female",
                "age": 26,
                "skills": "Delphi, pascal, fortran, basic"
            }
        ]


if __name__ == "__main__":
    unittest.main()

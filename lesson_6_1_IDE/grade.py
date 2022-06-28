def get_grade(grade):
    try:
        g = int(grade)
    except:
        return "Ошибка"

    dict = {
        2: "Плохо",
        3: "Удовлетворительно",
        4: "Хорошо",
        5: "Отлично"
        }

    if g < 2 or g > 5:
        return "Ошибка"

    return dict[g]


# Код вашей функции должен быть выше

try:
    assert get_grade(2) == "Плохо"
    assert get_grade(3) == "Удовлетворительно"
    assert get_grade(4) == "Хорошо"
    assert get_grade(5) == "Отлично"
    assert get_grade("") == "Ошибка"
except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")
else:
    print("Все хорошо, все работает")
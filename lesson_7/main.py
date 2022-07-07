import helpers


def run():
    print("Введите номер студента")
    user_pk = 0
    try:
        user_pk = int(input(">> "))
    except:
        pass
    pass

    print(user_pk)

    students = helpers.load_students(helpers.STUDENTS_FILENAME)
    professions = helpers.load_professions(helpers.PROFESSION_FILENAME)

    student = helpers.get_student_by_pk(students, user_pk)
    if student == None:
        print("У нас нет такого студента")
        exit(0)

    show_student_info(student)

    print("Выберите специальность для оценки студента Jane Snake")
    profession_name = input(">> ")
    profession = helpers.get_profession_by_title(professions, profession_name)

    if profession == None:
        print("У нас нет такой специальности")
        exit(0)

    show_compare(student, profession)


def show_student_info(student):
    print(f'Студент {student["full_name"]}')
    print(f'Знает {",".join(student["skills"])}')


def show_compare(student, profession):
    compare_result = helpers.check_fitness(student, profession)
    print(f'Пригодность {compare_result["fit_percent"]}%')
    print(f'{student["full_name"]} знает {",".join(compare_result["has"])}')
    print(f'{student["full_name"]} не знает {",".join(compare_result["lacks"])}')


if __name__ == "__main__":
    run()

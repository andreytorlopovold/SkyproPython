def show_statistic(filename):
    """
    show statistic from file with format
    AAA 1
    BBB 2
    qwerty 3
    ...
    """
    history_list = []
    with open(filename, 'rt') as file:
        for line in file:
            history_list.append(line.rstrip('\n').split(' ')[1])
    print(f"Всего игр сыграно: {len(history_list)}")
    print(f"Максимальный рекорд: {max(history_list)}")

if __name__ == "__main__":
    show_statistic("history.txt")

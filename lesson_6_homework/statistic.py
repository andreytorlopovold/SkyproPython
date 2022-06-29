def show_statistic(filename):
    """
    Test
    """
    history_list = []
    with open(filename, 'rt') as file:
        for line in file:
            history_list.append(line.rstrip('\n').split(' ')[1])
    print(f"Всего игр сыграно: {len(history_list)}")
    print(f"Максимальный рекорд: {max(history_list)}")

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    show_statistic("history.txt")

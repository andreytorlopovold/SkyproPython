import game
import statistic

HISTORY_FILE = "history.txt"
WORDS_FILE = "words.txt"

def main():
    print("Введите ваше имя")
    user_name = input("> ")
    user_score = game.start_game(WORDS_FILE)
    save_history(user_name, user_score, HISTORY_FILE)
    statistic.show_statistic(HISTORY_FILE)

def save_history(name, score, filename):
    with open(filename, "a") as file:
        file.write(f"\n{name} {score}")


if __name__ == "__main__":
    main()
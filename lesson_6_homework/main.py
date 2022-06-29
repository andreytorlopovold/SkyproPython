import game
import statistic

HISTORY_FILE = "history.txt"
WORDS_FILE = "words.txt"

user_name = ""
user_score = 0

def main():
    print("Введите ваше имя")
    user_name = input("> ")
    game.start_game(WORDS_FILE)
    save_history(user_name, user_score, HISTORY_FILE)
    statistic.show_statistic(HISTORY_FILE)

def save_history(name, score, filename):
    with open(filename, "a") as file:
        file.write(f"{user_name} {user_score}")



if __name__ == "__main__":
    main()
from Utils import load_random_word
from Player import Player
from BasicWord import BasicWord


def main():
    print("Введите имя игрока")
    user_name = input("> ")
    player = Player(user_name)
    print(f'Привет, {player.user_name}')
    word = load_random_word()
    print(f'Составьте {len(word.subwords)} слов из слова {word.word})')
    print(f'Слова не должны быть короче 3 букв')
    print('Поехали, ваше первое слово?')

    while True:
        attempt_word = input()
        if attempt_word.upper() in ['СТОП', 'STOP']:
            print('Игра завершена')
            print(f'Вы угадали {len(player.words)} слов')
            exit(0)

        if word.check_word(attempt_word):
            print('Верно')
            player.add(attempt_word)
        else:
            print('Неверно')

        if len(word.subwords) == len(player.words):
            print('Cлова закончились, игра завершена!')
            print(f'Вы угадали {len(word.subwords)} слов')


if __name__ == '__main__':
    main()

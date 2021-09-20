import random
import os


def main():

    random_w = random_word()
    list_words = [w for w in random_w]
    bool_list = ["" for w in random_w]
    trimed_word = ""
    print(list_words)
    print(bool_list)
    print("Random word: ", random_w)
    print('Bienvenido al juego del ahorcado')
    print('Numero de letras de la palabra: ')

    while True:
        user_char = input('Ingresa una letra: ')

        while len(user_char) > 1:
            print("INGRESA SOLO 1 CARACTER")
            user_char = input('Ingresa una letra: ')

        for index, char in enumerate(random_w):
            if char == user_char:
                bool_list[index] = char

        for char in bool_list:
            if char == "":
                print('_', end=" ")
                os.system('cls')
                os.system('clear')
            print(char, end=" ")
        print('\n')

        if ''.join(bool_list) == random_w:
            print('GANASTE!')
            break


def random_word():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for word in f:
            words.append(word)
        words = list(map(str.strip, words))
        random_word = random.choice(words)

        random_word_filtered = random_word.maketrans('áéíóú', 'aeiou')
        random_w = random_word.translate(random_word_filtered)

    return random_w


if __name__ == '__main__':
    main()

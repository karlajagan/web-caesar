import string
from sys import argv, exit
from helpers import alphabet_position, rotate_character


def rotate_string(text,rot):
    encripted_message = ""
    for character in text:
        if character in string.whitespace \
        or character in string.punctuation \
        or character.isdigit():
            encripted_message += character
        else:
            encripted_message += rotate_character(character,rot)

    return encripted_message

def main():

    if len(argv) > 1:
        if argv[1].isdigit():
            rotation = int(argv[1])
        else:
            print('rotation must be a integer number ')
            exit()
    else:
       print('usage: python3 caesar.py number')
        exit()
    message = input("Type a message: ")
    print(rotate_string(message,rotation))

if __name__ == "__main__":
    main()

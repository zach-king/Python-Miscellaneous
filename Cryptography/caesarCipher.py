import pyperclip
import sys


def main(message=None, key=None, mode=None):
    if message == None:
        message = input("Enter a message: ")

    if key == None:
        key = int(input("Enter a key: "))

    if mode == None:
        mode = int(input("Encrypt (1) or Decrypt (0)? : "))

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    translated = ''
    message = message.upper()

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode:
                num = (num + key) % len(LETTERS)
            else:
                num = (num - key) % len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol

    print(translated)
    pyperclip.copy(translated)



if __name__ == '__main__':
    if len(sys.argv) >= 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
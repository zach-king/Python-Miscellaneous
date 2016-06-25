import sys


def main(ciphertext=None):
    if ciphertext == None:
        ciphertext = input("Enter Ciphertext: ")

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-=_+<>[]{},./?;:"\'\\|`~'

    for key in range(len(LETTERS)):
        translated = ''

        for symbol in LETTERS:
            if symbol in LETTERS:
                num = (LETTERS.find(symbol) - key) % len(LETTERS)

                translated += LETTERS[num]
            else:
                translated += symbol
        print('Key %i: %s\n' % (key, translated))



if __name__ == '__main__':
    if len(sys.argv) != 1:
        main(sys.argv[1])
    else:
        main()
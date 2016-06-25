import sys
import pyperclip
import math

def encrypt(key, message):
    ciphertext = [''] * key
    
    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key

    return ''.join(ciphertext)


def decrypt(key, ciphertext):
    numColumns = math.ceil(len(ciphertext) / key)
    numRows = key
    numEmptyCells = (numColumns * numRows) - len(ciphertext)

    plaintext = [''] * numColumns
    col = 0
    row = 0

    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1

        if (col == numColumns) or (col == numColumns - 1 and row >= numRows - numEmptyCells):
            col = 0
            row += 1

    return ''.join(plaintext)


def main(key=None, message=None, mode=None):
    if key == None:
        key = int(input("Enter a Key: "))
    if message == None:
        message = input("Enter a Message: ")
    if mode == None:
        mode = int(input("Encrypt(1) or Decrypt(0): "))

    if mode:
        encrypted = encrypt(key, message)
        print(encrypted)
        pyperclip.copy(encrypted)
    else:
        decrypted = decrypt(key, message)
        print(decrypted)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
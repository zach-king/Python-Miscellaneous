# Reverse Cipher

def main():
    message = input('Enter a message: ')
    translated = message[::-1]
    print(translated)


if __name__ == '__main__':
    main()
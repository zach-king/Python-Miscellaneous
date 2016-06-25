import random, sys, transpositionCipher

NUM_TESTS = 20
SEED = 42

def main():
    global NUM_TESTS, SEED
    random.seed(SEED)

    for i in range(NUM_TESTS):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Test #%i: "%s..."' % (i+1, message[:50]))

        for key in range(1, len(message)):
            encrypted = transpositionCipher.encrypt(key, message)
            decrypted = transpositionCipher.decrypt(key, encrypted)

            if message != decrypted:
                print('Mismatch with key %i and message %s.' % (key, message))
                print(decrypted)
                sys.exit()

    print('transposition cipher test passed.')



if __name__ == '__main__':
    main()
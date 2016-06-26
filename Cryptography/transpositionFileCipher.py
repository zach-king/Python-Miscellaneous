import time, os, sys, transpositionCipher

def main(fname=None, key=None, mode=None):
    if fname == None:
        fname = input("Enter Filename: ")
    if key == None:
        key = int(input("Enter Key: "))
    if mode == None:
        mode = int(input("Encrypt(1) or Decrypt(0): "))

    if mode:
        mode = 'encrypt'
    else:
        mode = 'decrypt'

    outputFilename = fname + '.enc'

    if not os.path.exists(fname):
        print('The file "%s" does not exist. Quitting...' % fname)
        sys.exit()

    if os.path.exists(outputFilename):
        print('This will overwrite the file "%s". (C)ontinue or (Q)uit? ' % outputFilename)
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    with open(fname, 'r') as fileObj:
        content = fileObj.read()

    print('%sing...' % mode.title())

    startTime = time.time()

    if mode == 'encrypt':
        translated = transpositionCipher.encrypt(key, content)
    elif mode == 'decrypt':
        translated = transpositionCipher.decrypt(key, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (mode.title(), str(totalTime)))

    with open(outputFilename, 'w') as outputFileObj:
        outputFileObj.write(translated)

    print('Done %sing "%s" (%s characters).' % (mode, fname, str(len(content))))
    print('%sed file is "%s".' % (mode.title(), outputFilename))



if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
import hashlib
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python file-hash.py <file>')
        sys.exit(1)

    hasher = hashlib.md5()
    with open(sys.argv[1], 'rb') as f:
        buf = f.read()
        hasher.update(buf)

    print(hasher.hexdigest())



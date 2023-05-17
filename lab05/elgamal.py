import sys
from functions import generate_keys, encrypt, decrypt, sign, verify

# Autor: Wojciech Gola


def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print("Wrong number of arguments!")
        return

    arg = args[0]

    if arg == "-k":
        generate_keys()
    elif arg == "-e":
        encrypt()
    elif arg == "-d":
        decrypt()
    elif arg == "-s":
        sign()
    elif arg == "-v":
        verify()
    else:
        print("Wrong argument!")


if __name__ == "__main__":
    main()

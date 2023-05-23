import sys
from encrypt_functions import encrypt_1, encrypt_2, encrypt_3,  encrypt_4
from detect_functions import detect_1, detect_2, detect_3, detect_4

# Autor: Wojciech Gola


def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print("Wrong number of arguments!")
        return

    if args[0] == "-e":
        if args[1] == "-1":
            encrypt_1()
        elif args[1] == "-2":
            encrypt_2()
        elif args[1] == "-3":
            encrypt_3()
        elif args[1] == "-4":
            encrypt_4()
        else:
            print("Wrong argument!")

    elif args[0] == "-d":
        if args[1] == "-1":
            detect_1()
        elif args[1] == "-2":
            detect_2()
        elif args[1] == "-3":
            detect_3()
        elif args[1] == "-4":
            detect_4()
        else:
            print("Wrong argument!")
    else:
        print("Wrong argument!")


if __name__ == "__main__":
    main()

import sys
from prepare import prepare
# Autor: Wojciech Gola


def main():
    possible_options = ["-p", "-e", "-k"]

    if len(sys.argv) != 2:
        print("Wrong number of arguments!")
        return

    option = sys.argv[1]

    if option not in possible_options:
        print("Wrong argument!")
        return

    if option == "-p":
        prepare()
    elif option == "-e":
        print("encrypt")
    else:
        print("cryptoanalysis")


if __name__ == "__main__":
    main()

import sys
import os
from cesar_cypher import CesarCypher
from affine_cypher import AffineCypher


def exit():
    input("Press any key to exit...")


def main():
    PATH = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))

    first_arguments = ["-c", "-a"]
    second_arguments = ["-e", "-d", "-j", "-k"]

    given_args = sys.argv

    if len(given_args) != 3:
        print("Wrong number of arguments!")
        return exit()

    if given_args[1] not in first_arguments:
        print("Wrong first argument!")
        return exit()

    if given_args[2] not in second_arguments:
        print("Wrong second argument!")
        return exit()

    if given_args[1] == "-c":
        cypher = CesarCypher(PATH, given_args[2])
    else:
        cypher = AffineCypher(PATH, given_args[2])

    print(cypher)
    return exit()


if __name__ == "__main__":
    main()

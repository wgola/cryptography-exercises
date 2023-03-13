import sys
from src.caesar_cypher import CesarCypher
from src.affine_cypher import AffineCypher


# Autor: Wojciech Gola

def exit():
    input("Press 'Enter' to exit...")


def main():
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
        cypher = CesarCypher()
    else:
        cypher = AffineCypher()

    if given_args[2] == "-e":
        cypher.encrypt()
    elif given_args[2] == "-d":
        cypher.decrypt()
    elif given_args[2] == "-j":
        cypher.cryptoanalysis_plain()
    else:
        cypher.cryptoanalysis_encrypted()

    return exit()


if __name__ == "__main__":
    main()

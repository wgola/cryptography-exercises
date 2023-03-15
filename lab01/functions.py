import os


def get_file(filename, option):
    return open(os.path.join(os.path.realpath(os.getcwd()), filename), option)


def nwd(a, b):
    return b if a % b == 0 else nwd(b, a % b)


def if_small_letter(letter_ascii):
    return 97 <= letter_ascii <= 122


def if_big_letter(letter_ascii):
    return 65 <= letter_ascii <= 90


def find_inverse_number(number, modulo):
    for i in range(1, modulo):
        if (number * i) % modulo == 1:
            return i
    return None

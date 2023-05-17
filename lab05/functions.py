from random import randint
from math import gcd

# Autor: Wojciech Gola


def message_string_to_int(filename):
    with open(filename) as file:
        text = file.readline()

    list_of_ascii = [ord(letter) for letter in text]
    list_of_strings = [str(number).zfill(3) for number in list_of_ascii]
    return int("".join(list_of_strings))


def message_int_to_string(message):
    string_message = "0" + str(message)
    result = ""
    for i in range(0, len(string_message), 3):
        result += chr(int(string_message[i:i+3]))

    return result


def generate_keys():
    with open("elgamal.txt") as elgamal:
        p = int(elgamal.readline())
        g = int(elgamal.readline())

    private_key = randint(2, p-1)

    public_key = pow(g, private_key, p)

    with open("private.txt", "w") as private_key_file:
        private_key_file.write(str(p) + "\n" + str(g) +
                               "\n" + str(private_key))

    with open("public.txt", "w") as public_key_file:
        public_key_file.write(str(p) + "\n" + str(g) + "\n" + str(public_key))

    print("Keys generated.")


def encrypt():
    with open("public.txt") as public_key_file:
        p = int(public_key_file.readline())
        g = int(public_key_file.readline())
        public_key = int(public_key_file.readline())

    message = message_string_to_int("plain.txt")

    if message >= p:
        print("Error: message >= p")
        return

    k = randint(2, p-1)

    first_elem = str(pow(g, k, p))
    second_elem = str(((message % p) * pow(public_key, k, p)) % p)

    with open("crypto.txt", "w") as crypto_file:
        crypto_file.write(first_elem + "\n" + second_elem)

    print("Message encrypted.")


def decrypt():
    with open("private.txt") as private_key_file:
        p = int(private_key_file.readline())
        g = int(private_key_file.readline())
        private_key = int(private_key_file.readline())

    with open("crypto.txt") as crypto_file:
        first_elem = int(crypto_file.readline())
        second_elem = int(crypto_file.readline())

    key = pow(first_elem, private_key, p)
    inverse_key = pow(key, -1, p)

    with open("decrypt.txt", "w") as decrypted_file:
        decrypted_file.write(message_int_to_string(
            (second_elem * inverse_key) % p))

    print("Message decrypted.")


def sign():
    with open("private.txt") as private_key_file:
        p = int(private_key_file.readline())
        g = int(private_key_file.readline())
        private_key = int(private_key_file.readline())

    message = message_string_to_int("message.txt")

    if message >= p:
        print("Error: message >= p")
        return

    k = randint(2, p-2)
    while gcd(k, p - 1) != 1:
        k = randint(2, p-2)

    first_elem = pow(g, k, p)
    second_elem = int(
        ((message - private_key * first_elem) * pow(k, -1, p-1)) % (p-1))

    with open("signature.txt", "w") as signature_file:
        signature_file.write(str(first_elem) + "\n" + str(second_elem))

    print("Message signed.")


def verify():
    with open("public.txt") as public_key_file:
        p = int(public_key_file.readline())
        g = int(public_key_file.readline())
        public_key = int(public_key_file.readline())

    message = message_string_to_int("message.txt")

    with open("signature.txt") as signature_file:
        first_elem = int(signature_file.readline())
        second_elem = int(signature_file.readline())

    first_value = pow(g, message, p)
    second_value = pow(first_elem, second_elem, p) * \
        pow(public_key, first_elem, p)

    with open("verify.txt", "w") as verify_file:
        verify_file.write(str(first_value == (second_value % p)))

    print("Verification result:", first_value == (second_value % p))

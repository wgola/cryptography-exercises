import os


class Cypher:
    PATH = os.path.realpath(os.getcwd())
    print(PATH)

    def __init__(self, type):
        self.type = type

    def __get_file(self, filename, option):
        return open(os.path.join(self.PATH, filename), option)

    def __nwd(self, a, b):
        return b if a % b == 0 else self.__nwd(b, a % b)

    def __get_keys(self, keys):
        key = (
            int(keys[0]), 1) if self.type == "-c" else (int(keys[0]), int(keys[1]))

        if 0 <= key[0] <= 25 and self.__nwd(key[1], 26) == 1 and self.__find_inverse_number(key[1]) is not None:
            return key
        else:
            raise ValueError

    def __if_small_letter(self, letter_ascii):
        return 97 <= letter_ascii <= 122

    def __if_big_letter(self, letter_ascii):
        return 65 <= letter_ascii <= 90

    def __encrypt_text(self, text, key):
        result = ""

        for letter in text:
            letter_ascii = ord(letter)

            if self.__if_big_letter(letter_ascii):
                moved_letter = 65 + \
                    (key[1] * (letter_ascii - 65) + key[0]) % 26
            elif self.__if_small_letter(letter_ascii):
                moved_letter = 97 + \
                    (key[1] * (letter_ascii - 97) + key[0]) % 26
            else:
                moved_letter = letter_ascii

            result += chr(moved_letter)

        return result

    def encrypt(self):
        try:
            plain_text_file = self.__get_file("plain.txt", "r")
            key_file = self.__get_file("key.txt", "r")
        except:
            print("No 'plain.txt' or 'key.txt' file!")
            return

        plain_text = plain_text_file.readline()
        keys = key_file.readline().split(" ")

        try:
            key = self.__get_keys(keys)
        except:
            print("Not a valid key!")
            return

        encrypted_text = self.__encrypt_text(plain_text, key)

        encrypted_text_file = self.__get_file("crypto.txt", "w")
        encrypted_text_file.write(encrypted_text)
        print("Text encrypted succesully!")

        plain_text_file.close()
        key_file.close()
        encrypted_text_file.close()

    def __find_inverse_number(self, number):
        for i in range(1, 26):
            if (number * i) % 26 == 1:
                return number
        return None

    def __decrypt_text(self, text, key):
        result = ""

        inverse_number = self.__find_inverse_number(key[1])

        for letter in text:
            letter_ascii = ord(letter)

            if self.__if_big_letter(letter_ascii):
                moved_letter = 65 + \
                    ((inverse_number * (letter_ascii - 65) - key[0]) % 26)
            elif self.__if_small_letter(letter_ascii):
                moved_letter = 97 + \
                    ((inverse_number * (letter_ascii - 97) - key[0]) % 26)
            else:
                moved_letter = letter_ascii

            result += chr(moved_letter)

        return result

    def decrypt(self):
        try:
            cyphered_text_file = self.__get_file("crypto.txt", "r")
            key_file = self.__get_file("key.txt", "r")
        except:
            print("No 'crypto.txt' or 'key.txt' file!")
            return

        cyphered_text = cyphered_text_file.readline()
        keys = key_file.readline().split(" ")

        try:
            key = self.__get_keys(keys)
        except:
            print("Not a valid key!")
            return

        decrypted_text = self.__decrypt_text(cyphered_text, key)

        decrypted_text_file = self.__get_file("decrypt.txt", "w")
        decrypted_text_file.write(decrypted_text)
        print("Text decrypted succesfully!")

        cyphered_text_file.close()
        key_file.close()
        decrypted_text_file.close()

    def cryptoanalysis_with_plain_text(self):
        try:
            encrypted_text_file = self.__get_file("crypto.txt", "r")
            extra_text_file = self.__get_file("extra.txt", "r")
        except:
            print("No 'crypto.txt' or 'extra.txt' file!")
            return

        encrypted_text = encrypted_text_file.readline()
        extra_text = extra_text_file.readline()

        found_key = self.__analize_with_plain_text(encrypted_text, extra_text)
        decrypted_text = self.__decrypt_text(encrypted_text, found_key)

        decrypted_text_file, found_key_file = self.__get_file(
            "decrypt.txt", "w"), self.__get_file("key-found.txt", "w")

        decrypted_text_file.write(decrypted_text)
        found_key_file.write("{} {}".format(*found_key))
        print("Text deciphered succesfully!")

        encrypted_text_file.close()
        extra_text_file.close()
        decrypted_text_file.close()
        found_key_file.close()

    def __analize_with_plain_text(self, encrypted_text, plain_text):
        if self.type == "-c":
            plain_letter_ascii = ord(plain_text[0])
            encrypted_letter_ascii = ord(encrypted_text[0])
            difference = abs(plain_letter_ascii - encrypted_letter_ascii)
            return (26 - difference, 1) if plain_letter_ascii > encrypted_letter_ascii else (difference, 1)
        else:
            encrypted_letters_ascii = [ord(letter)
                                       for letter in encrypted_text]
            plain_letters_ascii = [ord(letter) for letter in plain_text]
            for i in range(0, len(plain_letters_ascii) - 1):
                a = (encrypted_letters_ascii[i] - encrypted_letters_ascii[i+1]) / (
                    plain_letters_ascii[i] - plain_letters_ascii[i+1])
                print(a)

    def cryptoanalysis_with_cryptogram(self):
        try:
            encrypted_text_file = self.__get_file("crypto.txt", "r")
        except:
            print("No 'crypto.txt' file!")

        encrypted_text = encrypted_text_file.readline()
        possible_keys = self.__generate_keys()

        possible_decryptions = [self.__decrypt_text(
            encrypted_text, key) + '\n' for key in possible_keys]

        decrypted_text_file = self.__get_file("decrypt.txt", "w")
        decrypted_text_file.writelines(possible_decryptions)
        print("Generated all possible decryptions!")

        encrypted_text_file.close()
        decrypted_text_file.close()

    def __generate_keys(self):
        if self.type == "-c":
            return [(key, 1) for key in range(1, 26)]
        else:
            result = []
            for a in range(1, 26):
                result.append(*[(a, b) for b in range(26) if self.__nwd(b, 26)
                              == 1 and self.__find_inverse_number(b) is not None])
            return result


if __name__ == "__main__":
    test = Cypher("-a")
    test.decrypt()

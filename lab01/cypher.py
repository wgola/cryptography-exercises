from functions import get_file, nwd, if_small_letter, if_big_letter, find_inverse_number


class Cypher:

    def __init__(self, type):
        self.type = type

    def encrypt(self):
        try:
            plain_text_file, key_file = get_file(
                "plain.txt", "r"), get_file("key.txt", "r")
        except:
            print("No 'plain.txt' or 'key.txt' file!")
            return

        plain_text, keys = plain_text_file.readline(), key_file.readline().split(" ")

        try:
            key = self.__get_keys(keys)
        except:
            print("Not a valid key!")
            return

        encrypted_text = self.__encrypt_text(plain_text, key)

        encrypted_text_file = get_file("crypto.txt", "w")
        encrypted_text_file.write(encrypted_text)

        print("Text encrypted succesully!")

        plain_text_file.close()
        key_file.close()
        encrypted_text_file.close()

    def decrypt(self):
        try:
            cyphered_text_file, key_file = get_file(
                "crypto.txt", "r"), get_file("key.txt", "r")
        except:
            print("No 'crypto.txt' or 'key.txt' file!")
            return

        cyphered_text, keys = cyphered_text_file.readline(), key_file.readline().split(" ")

        try:
            key = self.__get_keys(keys)
        except:
            print("Not a valid key!")
            return

        decrypted_text = self.__decrypt_text(cyphered_text, key)

        decrypted_text_file = get_file("decrypt.txt", "w")
        decrypted_text_file.write(decrypted_text)

        print("Text decrypted succesfully!")

        cyphered_text_file.close()
        key_file.close()
        decrypted_text_file.close()

    def cryptoanalysis_with_plain_text(self):
        try:
            encrypted_text_file, extra_text_file = get_file(
                "crypto.txt", "r"), get_file("extra.txt", "r")
        except:
            print("No 'crypto.txt' or 'extra.txt' file!")
            return

        encrypted_text, extra_text = encrypted_text_file.readline(), extra_text_file.readline()

        try:
            found_key = self.__analize_with_plain_text(
                encrypted_text, extra_text)
        except:
            print("Couldn't calculate key!")
            return

        decrypted_text = self.__decrypt_text(encrypted_text, found_key)

        decrypted_text_file, found_key_file = get_file(
            "decrypt.txt", "w"), get_file("key-found.txt", "w")

        decrypted_text_file.write(decrypted_text)
        found_key_file.write("{} {}".format(*found_key))

        print("Text deciphered succesfully!")

        encrypted_text_file.close()
        extra_text_file.close()
        decrypted_text_file.close()
        found_key_file.close()

    def cryptoanalysis_with_cryptogram(self):
        try:
            encrypted_text_file = get_file("crypto.txt", "r")
        except:
            print("No 'crypto.txt' file!")

        encrypted_text, possible_keys = encrypted_text_file.readline(), self.__generate_keys()

        possible_decryptions = [self.__decrypt_text(
            encrypted_text, key) + '\n' for key in possible_keys]

        decrypted_text_file = get_file("decrypt.txt", "w")
        decrypted_text_file.writelines(possible_decryptions)

        print("Generated all possible decryptions!")

        encrypted_text_file.close()
        decrypted_text_file.close()

    def __get_keys(self, keys):
        key = (
            int(keys[0]), 1) if self.type == "-c" else (int(keys[0]), int(keys[1]))

        if 0 <= key[0] <= 25 and nwd(key[1], 26) == 1 and find_inverse_number(key[1], 26) is not None:
            return key
        else:
            raise ValueError

    def __encrypt_text(self, text, key):
        result = ""

        for letter in text:
            letter_ascii = ord(letter)

            if if_big_letter(letter_ascii):
                moved_letter = 65 + \
                    (key[1] * (letter_ascii - 65) + key[0]) % 26
            elif if_small_letter(letter_ascii):
                moved_letter = 97 + \
                    (key[1] * (letter_ascii - 97) + key[0]) % 26
            else:
                moved_letter = letter_ascii

            result += chr(moved_letter)

        return result

    def __decrypt_text(self, text, key):
        result = ""

        inverse_number = find_inverse_number(key[1], 26)

        for letter in text:
            letter_ascii = ord(letter)

            if if_big_letter(letter_ascii):
                moved_letter = 65 + \
                    (inverse_number * (letter_ascii - 65 - key[0])) % 26
            elif if_small_letter(letter_ascii):
                moved_letter = 97 + \
                    (inverse_number * (letter_ascii - 97 - key[0])) % 26
            else:
                moved_letter = letter_ascii

            result += chr(moved_letter)

        return result

    def __change_text_to_numbers(self, text):
        letters_ascii = []
        for letter in text:
            letter_ascii = ord(letter)

            if 65 <= letter_ascii <= 90:
                letters_ascii.append(letter_ascii - 65)
            elif 97 <= letter_ascii <= 122:
                letters_ascii.append(letter_ascii - 97)

        return letters_ascii

    def __first_equation(self, encryptedA, encryptedB, plainA, plainB):
        sign = - 1 if encryptedA - encryptedB < 0 else 1

        return lambda a: sign * (encryptedA - encryptedB) == sign * (plainA - plainB) * a % 26

    def __second_equation(self, encryptedB, A, plainB):
        return lambda b: encryptedB == (A * plainB + b) % 26

    def __analize_with_plain_text(self, encrypted_text, plain_text):
        if self.type == "-c":
            plain_letter_ascii, encrypted_letter_ascii = ord(
                plain_text[0]), ord(encrypted_text[0])
            difference = abs(plain_letter_ascii - encrypted_letter_ascii)

            return (26 - difference, 1) if plain_letter_ascii > encrypted_letter_ascii else (difference, 1)
        else:
            encrypted_letters_ascii, plain_letters_ascii = self.__change_text_to_numbers(
                encrypted_text), self.__change_text_to_numbers(plain_text)

            found_key = None

            for i in range(len(plain_letters_ascii)):
                for j in range(i + 1, len(plain_letters_ascii)):
                    if abs(plain_letters_ascii[i] - plain_letters_ascii[j]) == 13:
                        continue
                    else:
                        A, B = 0, 0
                        first_equation = self.__first_equation(
                            encrypted_letters_ascii[i], encrypted_letters_ascii[j], plain_letters_ascii[i], plain_letters_ascii[j])

                        for a in range(26):
                            if first_equation(a):
                                A = a
                                second_equation = self.__second_equation(
                                    encrypted_letters_ascii[j], A, plain_letters_ascii[j])

                                for b in range(26):
                                    if second_equation(b):
                                        B = b
                                        break

                                break

                        found_key = (B, A)
                        break

                if found_key is not None:
                    break

            if found_key is None:
                raise ValueError
            else:
                return found_key

    def __generate_keys(self):
        if self.type == "-c":
            return [(key, 1) for key in range(1, 26)]
        else:
            result = []
            for a in range(0, 26):
                result.extend([(a, b) for b in range(26) if nwd(b, 26)
                              == 1 and find_inverse_number(b, 26) is not None])

            return result

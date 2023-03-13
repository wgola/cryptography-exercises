from src.cypher import Cypher


class CesarCypher(Cypher):

    def encrypt(self):
        try:
            plain_file = self.get_file("plain.txt", "r")
            key_file = self.get_file("key.txt", "r")
        except:
            print("No 'plain.txt' or 'key.txt' file!")
            return

        plain_text = plain_file.readline()
        key = int(key_file.readline().split(" ")[0])

        if not self.check_key(key):
            print("Not a valid key!")
            return

        encrypted_text = self.__encrypt_text(plain_text, key)

        encrypted_file = self.get_file("crypto.txt", "w")
        encrypted_file.write(encrypted_text)
        print("Text encrypted succesfully!")

        plain_file.close()
        key_file.close()
        encrypted_file.close()

    def decrypt(self):
        try:
            cyphered_file = self.get_file("crypto.txt", "r")
            key_file = self.get_file("key.txt", "r")
        except:
            print("No 'crypto.txt' or 'key.txt' file!")
            return

        cyphered_text = cyphered_file.readline()
        key = int(key_file.readline().split(" ")[0])

        if not self.check_key(key):
            print("Not a valid key!")
            return

        decrypted_text = self.__decrypt_text(cyphered_text, key)

        decrypted_file = self.get_file("decrypt.txt", "w")
        decrypted_file.write(decrypted_text)
        print("Text decrypted sucesfully!")

        cyphered_file.close()
        key_file.close()
        decrypted_file.close()

    def cryptoanalysis_plain(self):
        try:
            encrypted_file = self.get_file("crypto.txt", "r")
            extra_file = self.get_file("extra.txt", "r")
        except:
            print("No 'crypto.txt' or 'extra.txt' file!")
            return

        encrypted_text = encrypted_file.readline()
        extra_text = extra_file.readline()

        found_key = self.__analize_with_plain(extra_text, encrypted_text)
        decrypted_text = self.__decrypt_text(encrypted_text, found_key)

        decrypted_file = self.get_file("decrypt.txt", "w")
        found_key_file = self.get_file("key-found.txt", "w")

        decrypted_file.write(decrypted_text)
        found_key_file.write(str(found_key))
        print("Text deciphered sucesfully!")

        encrypted_file.close()
        extra_file.close()
        decrypted_file.close()
        found_key_file.close()

    def cryptoanalysis_encrypted(self):
        try:
            encrypted_file = self.get_file("crypto.txt", "r")
        except:
            print("No 'crypto.txt' file!")
            return

        encrypted_text = encrypted_file.readline()

        decrypted_options = [self.__decrypt_text(
            encrypted_text, i) + "\n" for i in range(0, 26)]

        decrypted_file = self.get_file("decrypt.txt", "w")
        decrypted_file.writelines(decrypted_options)
        print("Generated all possible decipher options succesfully!")

        encrypted_file.close()
        decrypted_file.close()

    def check_key(self, key):
        return 0 <= key <= 25

    def __analize_with_plain(self, plain, encrypted):
        plain_letter_ascii = ord(plain[0])
        encrypted_letter_ascii = ord(encrypted[0])
        difference = abs(plain_letter_ascii - encrypted_letter_ascii)
        return 26 - difference if plain_letter_ascii > encrypted_letter_ascii else difference

    def __encrypt_text(self, text, key):
        result = ""

        for letter in text:
            ascii_number = ord(letter)

            if self.if_big_letter(ascii_number):
                moved_letter = 65 + (ascii_number - 65 + key) % 26
            elif self.if_small_letter(ascii_number):
                moved_letter = 97 + (ascii_number - 97 + key) % 26
            else:
                moved_letter = ascii_number

            result += chr(moved_letter)

        return result

    def __decrypt_text(self, text, key):
        result = ""
        for letter in text:
            ascii_number = ord(letter)

            if self.if_big_letter(ascii_number):
                moved_letter = 65 + (ascii_number - 65 - key) % 26
            elif self.if_small_letter(ascii_number):
                moved_letter = 97 + (ascii_number - 97 - key) % 26
            else:
                moved_letter = ascii_number

            result += chr(moved_letter)

        return result

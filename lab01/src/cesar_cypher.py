from cypher import Cypher
import os


class CesarCypher(Cypher):

    def __init__(self, path):
        self.path = path

    def encrypt(self):
        try:
            plain_file = open(os.path.join(self.path, "plain.txt"))
            key_file = open(os.path.join(self.path, "key.txt"))
        except:
            print("No 'plain.txt' or 'key.txt' file!")
            return

        plain_text = plain_file.readline()
        key = key_file.readline().split(" ")[0]

        x = self.__encrypt_text(plain_text, int(key))
        print(x)
        print(self.__decrypt_text(x, int(key)))

        plain_file.close()
        key_file.close()

    def decrypt(self):
        pass

    def cryptoanalysis_plain(self):
        pass

    def cryptoanalysis_encrypted(self):
        pass

    def __encrypt_text(self, text, key):
        result = ""
        for letter in text:
            number = ord(letter)

            changed_number = (
                number - 65 + key) % 26 if 65 <= number <= 90 else (number - 97 + key) % 26
            result += chr(65 + changed_number) if 65 <= number <= 90 else chr(97 + changed_number)

        return result

    def __decrypt_text(self, text, key):
        result = ""
        for letter in text:
            number = ord(letter)

            changed_number = (
                number - 65 + key) % 26 if 65 <= number <= 90 else (number - 97 + key) % 26
            result += chr(90 - changed_number) if 65 <= number <= 90 else chr(122 - changed_number)

        return result

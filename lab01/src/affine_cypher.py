from src.cypher import Cypher


class AffineCypher(Cypher):

    def encrypt(self):
        try:
            plain_file = self.get_file("plain.txt", "r")
            key_file = self.get_file("key.txt", "r")
        except:
            print("No 'plain.txt' or 'key.txt' file!")
            return

        plain_text = plain_file.readline()
        key_text = key_file.readline().split(" ")

        if len(key_text) != 2:
            print("Wrong length of key: expected two numbers!")
            return

        key = (int(key_text[0]), int(key_text[1]))

        if not self.check_key(key):
            print("Not a valid key!")

        encrypted_text = self.__encrypt_text(plain_text, key)

    def decrypt():
        pass

    def cryptoanalysis_plain():
        pass

    def cryptoanalysis_encrypted():
        pass

    def check_key(self, key):
        return 0 <= key[0] <= 25 and self.__nwd(key[1], 26) == 1

    def __nwd(self, a, b):
        return b if a % b == 0 else self.__nwd(b, a % b)

    def __encrypt_text(self, text, key):
        result = ""
        for letter in text:
            ascii_number = ord(letter)

            if self.if_big_letter(ascii_number):
                moved_letter = 65 + \
                    (key[1] * (ascii_number - 65) + key[0]) % 26
            elif self.if_small_letter(ascii_number):
                moved_letter = 97 + \
                    (key[1] * (ascii_number - 97) + key[0]) % 26
            else:
                moved_letter = ascii_number

            result += chr(moved_letter)

        return result

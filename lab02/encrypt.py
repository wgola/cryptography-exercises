# Autor: Wojciech Gola

def encrypt():
    try:
        with open("key.txt", "r") as key_file:
            key = key_file.readline()
            ascii_key = [ord(sign) for sign in key]

        with open("plain.txt", "r") as plain_file:
            plain_lines = plain_file.read().split("\n")
            ascii_lines = [[ord(sign) for sign in line]
                           for line in plain_lines]

        with open("crypto.txt", "w+") as crypto_file:
            for line in ascii_lines:
                encrypted_line = ""
                for i in range(len(key)):
                    binary_sign = format(line[i] ^ ascii_key[i], 'b')
                    if len(binary_sign) < 8:
                        binary_sign = (8 - len(binary_sign)) * \
                            '0' + binary_sign

                    encrypted_line += binary_sign

                crypto_file.write(encrypted_line + "\n")

        print("Text encrypted succesfully!")

    except:
        print("Files 'plain.txt' or 'key.txt' not found!")

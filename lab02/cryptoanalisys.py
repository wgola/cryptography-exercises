# Autor: Wojciech Gola

def cryptoanalysis():
    try:
        with open("crypto.txt", "r") as crypto_file:
            encrypted_text = crypto_file.read().split("\n")[:-1]

        encrypted_text_signs = []
        for row in encrypted_text:
            tmp_row = [row[i:i+8] for i in range(0, len(row), 8)]
            encrypted_text_signs.append(tmp_row)

        decrypted_text = encrypted_text_signs

        for row in encrypted_text_signs:
            for col_index, col in enumerate(row):
                if len(col) > 1:
                    if col[1] == "1":
                        for i in range(len(encrypted_text_signs)):
                            encrypted_sign = encrypted_text_signs[i][col_index]
                            encrypted_line = ""
                            encrypted_line = format(
                                int(encrypted_sign, 2) ^ int(col, 2), 'b')

                            if len(encrypted_line) < 8:
                                encrypted_line = (8 - len(encrypted_line)) * \
                                    "0" + encrypted_line

                            if encrypted_line == "00000000":
                                decrypted_text[i][col_index] = " "
                            else:
                                decrypted_text[i][col_index] = chr(
                                    int(encrypted_line, 2))

        decrypted_text = ["".join(line).lower() +
                          "\n" for line in decrypted_text]

        with open("decrypt.txt", "w+") as decrypt_file:
            decrypt_file.writelines(decrypted_text)

        print("Text decrypted succesfully!")

    except:
        print("File 'crypto.txt' not found!")

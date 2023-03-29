# Autor: Wojciech Gola

def prepare():
    try:
        with open("orig.txt", "r") as orig_file:
            orig_txt = orig_file.read().replace("\n", " ").lower()

        with open("plain.txt", "w+") as plain_file:
            new_line = ""
            for letter in orig_txt:
                new_line += letter
                if len(new_line) == 64:
                    plain_file.write(new_line + "\n")
                    new_line = ""

            if len(new_line) != 0:
                new_line += " " + (63 - len(new_line))*"x"
                plain_file.write(new_line)

        print("Text prepared succesfully!")

    except:
        print("File 'orig.txt' not found!")

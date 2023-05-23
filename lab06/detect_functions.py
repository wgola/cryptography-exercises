import re

# Autor: Wojciech Gola


def bin_to_hex(message):
    return hex(int(message, 2))[2:]


def detect_1():
    with open("watermark.html", "r") as watermark_file:
        data = watermark_file.readlines()

    message = ""

    for i in range(64):
        if data[i].endswith(" \n"):
            message += "1"
        else:
            message += "0"

    hex_message = bin_to_hex(message)

    with open("detect.txt", "w") as detect_file:
        detect_file.write(hex_message + "\n")

    print("Message detected.")


def detect_2():
    with open("watermark.html", "r") as watermark_file:
        data = list(watermark_file.read())

    all_spaces_positions = [pos for pos,
                            char in enumerate(data) if char == " "]
    message = ""
    i = 0
    while len(message) != 64:
        next_sign = data[all_spaces_positions[i] + 1]
        if next_sign == " ":
            message += "1"
            i += 2
        else:
            message += "0"
            i += 1

    hex_message = bin_to_hex(message)

    with open("detect.txt", "w") as detect_file:
        detect_file.write(hex_message + "\n")

    print("Message detected.")


def detect_3():
    with open("watermark.html", "r") as watermark_file:
        data = watermark_file.read()

    all_i_occurences = [m.start() for m in re.finditer("<i ", data)]

    message = ""
    for i in range(64):
        curr_position = all_i_occurences[i]
        curr_tag = data[curr_position:curr_position+49]
        if 'style="margin-bottom: 0cm; line-height: 100%"' in curr_tag:
            message += "0"
        elif 'style="margin-botom: 0cm; lineheight: 100%"' in curr_tag:
            message += "1"

    hex_message = bin_to_hex(message)

    with open("detect.txt", "w") as detect_file:
        detect_file.write(hex_message + "\n")

    print("Message detected.")


def detect_4():
    with open("watermark.html", "r") as watermark_file:
        data = watermark_file.read()

    all_i_opening_occurences = [m.start()
                                for m in re.finditer("<i></i><i>", data)]
    all_i_closing_occurences = [m.start()
                                for m in re.finditer("</i><i></i>", data)]
    all_ocurrences = [*all_i_opening_occurences,
                      *all_i_closing_occurences]
    all_ocurrences.sort()

    message = ""
    for i in range(64):
        curr_position = all_ocurrences[i]
        curr_tag = data[curr_position:curr_position+11]
        if "<i></i><i>" in curr_tag:
            message += "1"
        elif "</i><i></i>" in curr_tag:
            message += "0"

    hex_message = bin_to_hex(message)

    with open("detect.txt", "w") as detect_file:
        detect_file.write(hex_message + "\n")

    print("Message detected.")

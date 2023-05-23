import re

# Autor: Wojciech Gola


def hex_to_bin(message):
    return bin(int(message, 16))[2:].zfill(64)


def encrypt_1():
    with open("cover.html", "r") as cover_file:
        data = cover_file.readlines()

    with open("mess.txt", "r") as mess_file:
        message = mess_file.readline()

    binary_message = hex_to_bin(message)

    if len(data) < 64:
        print("Too little lines in cover.html!")
        return

    for i in range(64):
        if binary_message[i] == "1":
            curr_line = data[i]
            curr_line = curr_line.rstrip("\n")
            data[i] = curr_line + " \n"

    for i in range(64, len(data)):
        curr_line = data[i]
        curr_line = curr_line.rstrip("\n")
        data[i] = curr_line + " \n"

    with open("watermark.html", "w") as watermark_file:
        for line in data:
            watermark_file.write(line)

    print("Message encrypted.")


def encrypt_2():
    with open("cover.html", "r") as cover_file:
        data = list(cover_file.read())

    with open("mess.txt", "r") as mess_file:
        message = mess_file.readline()

    binary_message = hex_to_bin(message)
    all_spaces_positions = [pos for pos,
                            char in enumerate(data) if char == " "]

    if len(all_spaces_positions) < 64:
        print("Too little spaces in cover.html!")

    for i in range(64):
        if binary_message[i] == "1":
            data[all_spaces_positions[i]] = "  "

    for i in range(64, len(all_spaces_positions)):
        data[all_spaces_positions[i]] = "  "

    with open("watermark.html", "w") as watermark_file:
        watermark_file.write("".join(data))

    print("Message encrypted.")


def encrypt_3():
    with open("cover.html", "r") as cover_file:
        data = cover_file.read()

    with open("mess.txt", "r") as mess_file:
        message = mess_file.readline()

    all_i_occurences = [m.start() for m in re.finditer("<i>", data)]

    if len(all_i_occurences) < 64:
        print("Too little <i> tags in cover.html!")

    formatted_text = data
    binary_message = hex_to_bin(message)

    for i in range(64):
        changed_tag_style = ""
        if binary_message[i] == "0":
            changed_tag_style = '<i style="margin-bottom: 0cm; line-height: 100%">'
        else:
            changed_tag_style = '<i style="margin-botom: 0cm; lineheight: 100%">'

        tag_position = formatted_text.index("<i>")
        formatted_text = formatted_text[:tag_position] + \
            changed_tag_style + formatted_text[tag_position+3:]

    for i in range(64, len(all_i_occurences)):
        changed_tag_style = '<i style="margin-bottom: 0cm; line-height: 100%">'
        tag_position = formatted_text.index("<i>")
        formatted_text = formatted_text[:tag_position] + \
            changed_tag_style + formatted_text[tag_position+3:]

    with open("watermark.html", "w") as watermark_file:
        for line in formatted_text:
            watermark_file.write(line)

    print("Message encrypted.")


def encrypt_4():
    with open("cover.html", "r") as cover_file:
        data = cover_file.read()

    with open("mess.txt", "r") as mess_file:
        message = mess_file.readline()

    all_i_opening_occurences = [m.start() for m in re.finditer("<i>", data)]
    all_i_closing_occurences = [m.start() for m in re.finditer("</i>", data)]

    zipped_i_occurences = list(
        zip(all_i_opening_occurences, all_i_closing_occurences))

    if len(zipped_i_occurences) < 64:
        print("Too little <i> tags in cover.html!")

    formatted_text = data
    binary_message = hex_to_bin(message)

    shift = 0
    for i in range(64):
        curr_position = zipped_i_occurences[i]
        if binary_message[i] == "1":
            formatted_text = formatted_text[:curr_position[0] + shift] + \
                "<i></i><i>" + formatted_text[curr_position[0] + 3 + shift:]
        else:
            formatted_text = formatted_text[:curr_position[1] + shift] + \
                "</i><i></i>" + formatted_text[curr_position[1] + 4 + shift:]

        shift += 7

    for i in range(64, len(zipped_i_occurences)):
        curr_position = zipped_i_occurences[i]
        formatted_text = formatted_text[:curr_position[0] + shift] + \
            "<i></i><i>" + formatted_text[curr_position[0] + 3 + shift:]
        shift += 7

    with open("watermark.html", "w") as watermark_file:
        for line in formatted_text:
            watermark_file.write(line)

    print("Message encrypted.")

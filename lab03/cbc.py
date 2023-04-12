from save_image import save_image
from random import random


def cbc(input_image, block_size, key):
    image_width, image_height = input_image.size
    image_data = input_image.tobytes()

    encrypted_image_data = []
    previous_element = 278804 % 256

    for y in range(image_height):
        for x in range(image_width):
            current_pixel = image_data[y * image_width + x]
            xored_with_previous = current_pixel ^ previous_element

            encrypted_pixel = xored_with_previous ^ key[x %
                                                        block_size][y % block_size]

            previous_element = encrypted_pixel
            encrypted_image_data.append(encrypted_pixel)

    save_image(encrypted_image_data, "cbc_crypto.bmp",
               (image_width, image_height))

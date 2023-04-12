from save_image import save_image


def ecb(input_image, block_size, key):
    image_width, image_height = input_image.size
    image_data = input_image.tobytes()

    encrypted_image_data = []

    for y in range(image_height):
        for x in range(image_width):
            current_pixel = image_data[y * image_width + x]
            encrypted_pixel = current_pixel ^ key[x %
                                                  block_size][y % block_size]

            encrypted_image_data.append(encrypted_pixel)

    save_image(encrypted_image_data, "ecb_crypto.bmp",
               (image_width, image_height))

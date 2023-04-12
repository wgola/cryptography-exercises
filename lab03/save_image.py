from PIL import Image


def save_image(image_data, image_name, size):
    image_bytes = bytes(image_data)
    image = Image.frombytes("L", size, image_bytes)
    image.save(image_name)

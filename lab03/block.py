from hashlib import md5
from PIL import Image
from ecb import ecb
from cbc import cbc


def get_key(block_size):
    keys = []
    for x in range(block_size):
        key = md5(str(278804 * x).encode()).digest()
        keys.append(key)

    return keys


def main():
    input_image = Image.open("plain.bmp")

    BLOCK_SIZE = 8

    key = get_key(BLOCK_SIZE)

    ecb(input_image, BLOCK_SIZE, key)
    cbc(input_image, BLOCK_SIZE, key)


if __name__ == "__main__":
    main()

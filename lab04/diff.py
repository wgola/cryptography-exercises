import sys

# Autor: Wojciech Gola


def count_diff():

    if len(sys.argv) != 3:
        print("Wrong number of hashes!")
        return

    hash1, hash2 = sys.argv[1], sys.argv[2]

    if len(hash1) != len(hash2):
        print("Hashes are not same the length!")
        return

    bin_hash1 = bin(int(hash1, 16))[2:].zfill(8)
    bin_hash2 = bin(int(hash2, 16))[2:].zfill(8)

    different_bits = 0
    for bit in zip(bin_hash1, bin_hash2):
        if bit[0] != bit[1]:
            different_bits += 1

    bits_number = len(hash1) * 4

    percent = round(different_bits / bits_number, ndigits=3) * 100

    print("Liczba różniących się bitów: {} z {}, procentowo: {}%".format(
        different_bits, bits_number, percent))


if __name__ == "__main__":
    count_diff()

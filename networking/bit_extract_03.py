"""
Practice example: Bit Extract
Category: Networking
Variant: 3
"""


def extract_bits(value, offset, width):
    if offset < 0 or width <= 0:
        raise ValueError("invalid bit range")

    mask = (1 << width) - 1
    return (value >> offset) & mask


if __name__ == "__main__":
    value = 0b11010110
    print(extract_bits(value, 2, 3))

# Practice variant 3

"""
Practice example: Rms
Category: Signal Processing
Variant: 2
"""


import math


def rms(values):
    if not values:
        return 0.0

    mean_square = sum(value * value for value in values) / len(values)
    return math.sqrt(mean_square)


if __name__ == "__main__":
    print(rms([1, -1, 2, -2, 3, -3]))

# Practice variant 2

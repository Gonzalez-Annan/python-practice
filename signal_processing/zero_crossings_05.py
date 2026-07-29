"""
Practice example: Zero Crossings
Category: Signal Processing
Variant: 5
"""


def zero_crossings(values):
    crossings = []

    for i in range(1, len(values)):
        previous = values[i - 1]
        current = values[i]

        if previous == 0:
            continue

        if (previous < 0 <= current) or (previous > 0 >= current):
            crossings.append(i)

    return crossings


if __name__ == "__main__":
    samples = [-2, -1, 1, 2, -1, -3, 2]
    print(zero_crossings(samples))

# Practice variant 5

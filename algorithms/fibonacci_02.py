"""
Practice example: Fibonacci
Category: Algorithms
Variant: 2
"""


def fibonacci(count):
    if count <= 0:
        return []

    sequence = [0]

    if count == 1:
        return sequence

    sequence.append(1)

    while len(sequence) < count:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


if __name__ == "__main__":
    print(fibonacci(12))

# Practice variant 2

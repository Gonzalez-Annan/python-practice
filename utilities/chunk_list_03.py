"""
Practice example: Chunk List
Category: Utilities
Variant: 3
"""


def chunks(values, size):
    if size <= 0:
        raise ValueError("size must be positive")

    return [
        values[i:i + size]
        for i in range(0, len(values), size)
    ]


if __name__ == "__main__":
    print(chunks(list(range(10)), 3))

# Practice variant 3

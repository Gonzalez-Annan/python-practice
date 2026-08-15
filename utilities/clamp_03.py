"""
Practice example: Clamp
Category: Utilities
Variant: 3
"""


def clamp(value, minimum, maximum):
    if minimum > maximum:
        raise ValueError("minimum cannot exceed maximum")

    return max(minimum, min(value, maximum))


if __name__ == "__main__":
    for value in [-5, 3, 15]:
        print(clamp(value, 0, 10))

# Practice variant 3

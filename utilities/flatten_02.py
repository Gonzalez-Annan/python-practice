"""
Practice example: Flatten
Category: Utilities
Variant: 2
"""


def flatten(values):
    result = []

    for group in values:
        result.extend(group)

    return result


if __name__ == "__main__":
    print(flatten([[1, 2], [3], [4, 5, 6]]))

# Practice variant 2

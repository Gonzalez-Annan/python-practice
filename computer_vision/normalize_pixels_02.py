"""
Practice example: Normalize Pixels
Category: Computer Vision
Variant: 2
"""


def normalize_pixels(values):
    if not values:
        return []

    minimum = min(values)
    maximum = max(values)

    if maximum == minimum:
        return [0.0 for _ in values]

    return [
        (value - minimum) / (maximum - minimum)
        for value in values
    ]


if __name__ == "__main__":
    print(normalize_pixels([12, 15, 18, 21, 30]))

# Practice variant 2

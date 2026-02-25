"""
Practice example: Threshold
Category: Computer Vision
Variant: 4
"""


def threshold_image(image, threshold):
    return [
        [255 if pixel >= threshold else 0 for pixel in row]
        for row in image
    ]


if __name__ == "__main__":
    image = [
        [20, 80, 140],
        [200, 30, 170],
        [90, 110, 240],
    ]

    print(threshold_image(image, 128))

# Practice variant 4

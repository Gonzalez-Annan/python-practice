"""
Practice example: Bounding Box
Category: Computer Vision
Variant: 2
"""


def bounding_box(points):
    if not points:
        return None

    xs = [point[0] for point in points]
    ys = [point[1] for point in points]

    return min(xs), min(ys), max(xs), max(ys)


if __name__ == "__main__":
    points = [(3, 2), (8, 9), (2, 7), (6, 1)]
    print(bounding_box(points))

# Practice variant 2

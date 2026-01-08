"""
Practice example: Bubble Sort
Category: Algorithms
Variant: 2
"""


def bubble_sort(values):
    values = values.copy()

    for end in range(len(values) - 1, 0, -1):
        swapped = False

        for i in range(end):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swapped = True

        if not swapped:
            break

    return values


if __name__ == "__main__":
    print(bubble_sort([8, 3, 1, 7, 4, 2]))

# Practice variant 2

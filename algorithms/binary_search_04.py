"""
Practice example: Binary Search
Category: Algorithms
Variant: 4
"""


def binary_search(values, target):
    low = 0
    high = len(values) - 1

    while low <= high:
        mid = (low + high) // 2

        if values[mid] == target:
            return mid

        if values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    data = [1, 4, 7, 9, 13, 21, 42]
    print(binary_search(data, 13))

# Practice variant 4

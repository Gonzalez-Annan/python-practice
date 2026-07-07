"""
Practice example: Moving Average
Category: Signal Processing
Variant: 4
"""


def moving_average(values, window):
    if window <= 0:
        raise ValueError("window must be positive")

    output = []

    for i in range(len(values)):
        start = max(0, i - window + 1)
        section = values[start:i + 1]
        output.append(sum(section) / len(section))

    return output


if __name__ == "__main__":
    print(moving_average([1, 2, 8, 4, 5, 10], 3))

# Practice variant 4

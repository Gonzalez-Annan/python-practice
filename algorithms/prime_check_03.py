"""
Practice example: Prime Check
Category: Algorithms
Variant: 3
"""


def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


if __name__ == "__main__":
    for value in range(2, 30):
        if is_prime(value):
            print(value)

# Practice variant 3

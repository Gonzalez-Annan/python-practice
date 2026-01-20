"""
Practice example: Gcd
Category: Algorithms
Variant: 2
"""


def gcd(a, b):
    a = abs(a)
    b = abs(b)

    while b:
        a, b = b, a % b

    return a


if __name__ == "__main__":
    print(gcd(84, 30))

# Practice variant 2

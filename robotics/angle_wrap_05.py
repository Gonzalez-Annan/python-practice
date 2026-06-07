"""
Practice example: Angle Wrap
Category: Robotics
Variant: 5
"""


import math


def wrap_to_pi(angle):
    return (angle + math.pi) % (2 * math.pi) - math.pi


if __name__ == "__main__":
    for angle in [-7.0, -3.5, 0.0, 3.5, 7.0]:
        print(angle, wrap_to_pi(angle))

# Practice variant 5

"""
Practice example: Forward Kinematics 2Link
Category: Robotics
Variant: 3
"""


import math


def forward_kinematics(theta1, theta2, length1, length2):
    x = (
        length1 * math.cos(theta1)
        + length2 * math.cos(theta1 + theta2)
    )

    y = (
        length1 * math.sin(theta1)
        + length2 * math.sin(theta1 + theta2)
    )

    return x, y


if __name__ == "__main__":
    position = forward_kinematics(
        math.radians(30),
        math.radians(45),
        1.0,
        0.7
    )

    print(position)

# Practice variant 3

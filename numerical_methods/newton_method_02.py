"""
Practice example: Newton Method
Category: Numerical Methods
Variant: 2
"""


def newton_method(f, df, x0, tolerance=1e-8, max_iterations=100):
    x = x0

    for _ in range(max_iterations):
        derivative = df(x)

        if derivative == 0:
            raise ZeroDivisionError("derivative became zero")

        next_x = x - f(x) / derivative

        if abs(next_x - x) < tolerance:
            return next_x

        x = next_x

    return x


if __name__ == "__main__":
    root = newton_method(
        lambda x: x * x - 2,
        lambda x: 2 * x,
        1.0
    )
    print(root)

# Practice variant 2

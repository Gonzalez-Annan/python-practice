"""
Practice example: Euler Integration
Category: Numerical Methods
Variant: 1
"""


def euler_step(f, t, x, dt):
    return x + dt * f(t, x)


def simulate(f, x0, dt, steps):
    t = 0.0
    x = x0
    history = [(t, x)]

    for _ in range(steps):
        x = euler_step(f, t, x, dt)
        t += dt
        history.append((t, x))

    return history


if __name__ == "__main__":
    model = lambda t, x: -0.5 * x
    print(simulate(model, 1.0, 0.1, 10))

# Practice variant 1

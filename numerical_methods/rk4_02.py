"""
Practice example: Rk4
Category: Numerical Methods
Variant: 2
"""


def rk4_step(f, t, x, dt):
    k1 = f(t, x)
    k2 = f(t + dt / 2, x + dt * k1 / 2)
    k3 = f(t + dt / 2, x + dt * k2 / 2)
    k4 = f(t + dt, x + dt * k3)

    return x + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6


if __name__ == "__main__":
    model = lambda t, x: -x
    x = 1.0
    t = 0.0
    dt = 0.1

    for _ in range(10):
        x = rk4_step(model, t, x, dt)
        t += dt
        print(t, x)

# Practice variant 2

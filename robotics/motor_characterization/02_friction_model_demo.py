#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

TAU_COULOMB = 0.020
TAU_STATIC = 0.026
VISCOUS_COEFFICIENT = 0.0028
STRIBECK_VELOCITY = 0.05
STRIBECK_EXPONENT = 2.0


def friction_components(velocity):
    velocity = np.asarray(velocity)

    sign = np.sign(velocity)
    abs_velocity = np.abs(velocity)

    coulomb = TAU_COULOMB * sign
    viscous = VISCOUS_COEFFICIENT * velocity

    stribeck = (
        (TAU_STATIC - TAU_COULOMB)
        * np.exp(
            -(
                abs_velocity
                / STRIBECK_VELOCITY
            ) ** STRIBECK_EXPONENT
        )
        * sign
    )

    total = coulomb + viscous + stribeck

    return coulomb, viscous, stribeck, total


def main():
    velocity = np.linspace(-1.0, 1.0, 2000)

    coulomb, viscous, stribeck, total = friction_components(velocity)

    plt.figure(figsize=(10, 6))
    plt.plot(velocity, coulomb, label="Coulomb friction")
    plt.plot(velocity, viscous, label="Viscous friction")
    plt.plot(velocity, stribeck, label="Stribeck contribution")
    plt.plot(velocity, total, linewidth=2, label="Total friction")

    plt.axhline(0, linewidth=0.8)
    plt.axvline(0, linewidth=0.8)

    plt.xlabel("Velocity [rad/s]")
    plt.ylabel("Friction torque [Nm]")
    plt.title("Motor Friction Model Components")

    plt.grid()
    plt.legend()
    plt.tight_layout()

    output = "friction_model_demo.png"
    plt.savefig(output, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"Saved: {output}")


if __name__ == "__main__":
    main()

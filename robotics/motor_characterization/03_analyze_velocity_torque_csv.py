#!/usr/bin/env python3

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    from scipy.optimize import curve_fit
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False


def coulomb_viscous_model(velocity, tau_c, b, offset):
    return tau_c * np.sign(velocity) + b * velocity + offset


def stribeck_model(
    velocity,
    tau_c,
    tau_s,
    w_s,
    b,
    offset,
    exponent,
):
    abs_velocity = np.abs(velocity)

    magnitude = (
        tau_c
        + (tau_s - tau_c)
        * np.exp(
            -(
                abs_velocity / w_s
            ) ** exponent
        )
    )

    return np.sign(velocity) * magnitude + b * velocity + offset


def fit_coulomb_viscous(velocity, torque):
    X = np.column_stack(
        [
            np.sign(velocity),
            velocity,
            np.ones_like(velocity),
        ]
    )

    parameters, _, _, _ = np.linalg.lstsq(
        X,
        torque,
        rcond=None,
    )

    tau_c, b, offset = parameters

    prediction = coulomb_viscous_model(
        velocity,
        tau_c,
        b,
        offset,
    )

    ss_res = np.sum((torque - prediction) ** 2)
    ss_tot = np.sum((torque - np.mean(torque)) ** 2)

    r_squared = (
        1.0 - ss_res / ss_tot
        if ss_tot > 0
        else np.nan
    )

    return tau_c, b, offset, r_squared


def fit_stribeck(velocity, torque):
    if not SCIPY_AVAILABLE:
        return None

    initial_guess = [
        0.02,
        0.03,
        0.05,
        0.003,
        0.0,
        2.0,
    ]

    lower_bounds = [
        0.0,
        0.0,
        0.0001,
        0.0,
        -0.1,
        0.2,
    ]

    upper_bounds = [
        1.0,
        1.0,
        5.0,
        1.0,
        0.1,
        10.0,
    ]

    parameters, _ = curve_fit(
        stribeck_model,
        velocity,
        torque,
        p0=initial_guess,
        bounds=(lower_bounds, upper_bounds),
        maxfev=100000,
    )

    prediction = stribeck_model(
        velocity,
        *parameters,
    )

    ss_res = np.sum((torque - prediction) ** 2)
    ss_tot = np.sum((torque - np.mean(torque)) ** 2)

    r_squared = (
        1.0 - ss_res / ss_tot
        if ss_tot > 0
        else np.nan
    )

    return parameters, r_squared


def main():
    parser = argparse.ArgumentParser(
        description="Analyze motor velocity/torque characterization data."
    )

    parser.add_argument(
        "csv",
        type=Path,
        help="Input CSV file",
    )

    parser.add_argument(
        "--low-speed-limit",
        type=float,
        default=0.5,
    )

    args = parser.parse_args()

    df = pd.read_csv(args.csv)

    required = {
        "command_velocity_rad_s",
        "measured_velocity_rad_s",
        "torque_Nm",
    }

    missing = required - set(df.columns)

    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    print(f"Loaded {len(df)} samples")

    summary = (
        df.groupby("command_velocity_rad_s")
        .agg(
            mean_velocity=("measured_velocity_rad_s", "mean"),
            std_velocity=("measured_velocity_rad_s", "std"),
            mean_torque=("torque_Nm", "mean"),
            std_torque=("torque_Nm", "std"),
            samples=("torque_Nm", "size"),
        )
        .reset_index()
        .sort_values("command_velocity_rad_s")
    )

    print()
    print("=== Summary ===")
    print(
        summary.to_string(
            index=False,
            float_format=lambda x: f"{x:.6f}",
        )
    )

    nonzero = summary[
        np.abs(summary["mean_velocity"]) > 1e-6
    ]

    velocity = nonzero["mean_velocity"].to_numpy()
    torque = nonzero["mean_torque"].to_numpy()

    tau_c, b, offset, r2 = fit_coulomb_viscous(
        velocity,
        torque,
    )

    print()
    print("=== Coulomb + viscous model ===")
    print(f"Coulomb friction:    {tau_c:.6f} Nm")
    print(f"Viscous coefficient: {b:.6f} Nm/(rad/s)")
    print(f"Offset:              {offset:.6f} Nm")
    print(f"R^2:                 {r2:.6f}")

    low_speed = nonzero[
        np.abs(nonzero["mean_velocity"]) <= args.low_speed_limit
    ]

    stribeck_result = fit_stribeck(
        low_speed["mean_velocity"].to_numpy(),
        low_speed["mean_torque"].to_numpy(),
    )

    if stribeck_result is not None:
        parameters, stribeck_r2 = stribeck_result

        (
            s_tau_c,
            tau_s,
            w_s,
            s_b,
            s_offset,
            exponent,
        ) = parameters

        print()
        print("=== Stribeck model ===")
        print(f"Coulomb torque:      {s_tau_c:.6f} Nm")
        print(f"Static torque:       {tau_s:.6f} Nm")
        print(f"Stribeck velocity:   {w_s:.6f} rad/s")
        print(f"Viscous coefficient: {s_b:.6f} Nm/(rad/s)")
        print(f"Offset:              {s_offset:.6f} Nm")
        print(f"Exponent:            {exponent:.6f}")
        print(f"R^2:                 {stribeck_r2:.6f}")

    elif not SCIPY_AVAILABLE:
        print()
        print("SciPy unavailable: skipping nonlinear Stribeck fit.")

    plt.figure(figsize=(9, 6))

    plt.errorbar(
        summary["mean_velocity"],
        summary["mean_torque"],
        yerr=summary["std_torque"],
        fmt="o",
        capsize=3,
        label="Measured",
    )

    velocity_plot = np.linspace(
        velocity.min(),
        velocity.max(),
        1000,
    )

    plt.plot(
        velocity_plot,
        coulomb_viscous_model(
            velocity_plot,
            tau_c,
            b,
            offset,
        ),
        label="Coulomb + viscous fit",
    )

    plt.xlabel("Velocity [rad/s]")
    plt.ylabel("Torque [Nm]")
    plt.title("Motor Friction Characterization")
    plt.grid()
    plt.legend()
    plt.tight_layout()

    output = args.csv.with_name(
        args.csv.stem + "_friction_analysis.png"
    )

    plt.savefig(
        output,
        dpi=150,
        bbox_inches="tight",
    )

    plt.close()

    print()
    print(f"Saved plot: {output}")


if __name__ == "__main__":
    main()

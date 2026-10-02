#!/usr/bin/env python3

import math

ENCODER_COUNTS_PER_REV = 2**20
VELOCITY_UNIT_RPM = 0.001
RATED_TORQUE_NM = 2.222


def counts_to_radians(counts, counts_per_rev=ENCODER_COUNTS_PER_REV):
    return counts * 2.0 * math.pi / counts_per_rev


def radians_to_counts(angle_rad, counts_per_rev=ENCODER_COUNTS_PER_REV):
    return angle_rad * counts_per_rev / (2.0 * math.pi)


def rpm_to_rad_s(rpm):
    return rpm * 2.0 * math.pi / 60.0


def rad_s_to_rpm(rad_s):
    return rad_s * 60.0 / (2.0 * math.pi)


def drive_velocity_to_rad_s(raw_velocity):
    rpm = raw_velocity * VELOCITY_UNIT_RPM
    return rpm_to_rad_s(rpm)


def rad_s_to_drive_velocity(rad_s):
    rpm = rad_s_to_rpm(rad_s)
    return rpm / VELOCITY_UNIT_RPM


def raw_torque_to_nm(raw_torque):
    return raw_torque / 1000.0 * RATED_TORQUE_NM


def main():
    counts = 641_868
    angle = counts_to_radians(counts)

    print("=== Encoder conversion ===")
    print(f"{counts} counts = {angle:.6f} rad")

    print()
    print("=== Velocity conversion ===")

    command = 0.1
    rpm = rad_s_to_rpm(command)
    drive_units = rad_s_to_drive_velocity(command)

    print(f"{command:.3f} rad/s = {rpm:.6f} rpm")
    print(f"{command:.3f} rad/s = {drive_units:.1f} raw mRPM units")

    print()
    print("=== One revolution per second ===")
    one_rev_per_second = 2.0 * math.pi
    print(f"1 rev/s = {one_rev_per_second:.6f} rad/s")
    print(f"1 rev/s = {rad_s_to_rpm(one_rev_per_second):.2f} rpm")

    print()
    print("=== Torque conversion ===")

    for raw in [4, 8, 11, 15, 100, 1000]:
        print(f"{raw:4d} raw -> {raw_torque_to_nm(raw):.6f} Nm")


if __name__ == "__main__":
    main()

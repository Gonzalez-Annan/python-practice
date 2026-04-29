"""
Practice example: Ipv4 Parser
Category: Networking
Variant: 5
"""


def parse_ipv4(address):
    parts = address.split(".")

    if len(parts) != 4:
        raise ValueError("invalid IPv4 address")

    octets = []

    for part in parts:
        value = int(part)

        if not 0 <= value <= 255:
            raise ValueError("invalid IPv4 octet")

        octets.append(value)

    return octets


if __name__ == "__main__":
    print(parse_ipv4("192.168.1.10"))

# Practice variant 5

"""
Practice example: Hex Parser
Category: Networking
Variant: 2
"""


def parse_hex_bytes(value):
    cleaned = value.replace(" ", "").replace(":", "")

    if len(cleaned) % 2:
        raise ValueError("hex string must contain complete bytes")

    return [
        int(cleaned[i:i + 2], 16)
        for i in range(0, len(cleaned), 2)
    ]


if __name__ == "__main__":
    print(parse_hex_bytes("aa:10:ff:03"))

# Practice variant 2

"""
Practice example: Low Pass Filter
Category: Robotics
Variant: 4
"""


class LowPassFilter:
    def __init__(self, alpha):
        self.alpha = alpha
        self.value = None

    def update(self, sample):
        if self.value is None:
            self.value = sample
        else:
            self.value = (
                self.alpha * sample
                + (1 - self.alpha) * self.value
            )

        return self.value


if __name__ == "__main__":
    filt = LowPassFilter(0.2)

    for sample in [0, 10, 8, 12, 9, 10]:
        print(filt.update(sample))

# Practice variant 4

import random
import math
from arm import Arm

class UBC(object):

    def __init__(self, arm_n, n):
        self.arm_n = arm_n
        self.n = n
        self.arms = [Arm(math.fabs(random.random()), 1) for _ in range(arm_n)]
        self.counts = [0 for _ in range(arm_n)]
        self.rewards = [0.0 for _ in range(arm_n)]

    def calc_expected_values(self):
        expected_values = []
        for (c, r) in zip(self.counts, self.rewards):
            expected_values.append(r/c)
        return expected_values

    def calc_half_widths(self):
        half_widths = []
        R = math.fabs(max(self.rewards) - min(self.rewards))
        counts = self.counts
        for c in counts:
            half_widths.append(R * math.sqrt((2 * math.log1p(sum(counts)) / c)))

        return half_widths

    def exec_one(self):
        if 0 in self.counts:
            arm_i = self.counts.index(0)
        else:
            expected_values = self.calc_expected_values()
            half_widths = self.calc_half_widths()
            materials = [e+h for (e, h) in zip(expected_values, half_widths)]
            arm_i = materials.index(max(materials))

        result = self.arms[arm_i].pick()
        self.counts[arm_i] += 1
        self.rewards[arm_i] += result

    def exec(self):
        for i in range(self.n):
            self.exec_one()
        mus = [arm.mu for arm in self.arms]
        print('counts: ', self.counts)
        print('rewards: ', self.rewards)
        print('mus: ', mus)

ubc = UBC(4, 100000)
ubc.exec()

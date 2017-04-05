import random
import math
from arm import Arm

class EGreedy(object):

    def __init__(self, arm_n, n, e):
        self.arm_n = arm_n
        self.n = n
        self.e = e
        self.arms = [Arm(math.fabs(random.random()), 1) for _ in range(arm_n)]
        self.counts = [1 for _ in range(arm_n)]
        self.rewards = [1.0 for _ in range(arm_n)]
        self.search_n = 0

    def is_search(self):
        if random.random() < self.e:
            self.search_n += 1
            return True
        return False

    def exec_one(self):
        # pick a arm
        if self.is_search():
            arm_i = random.randrange(self.arm_n)
        else:
            means = [ r/c for (c, r) in zip(self.counts, self.rewards) ]
            top_mean = means.index(max(means))
            arm_i = top_mean
        # exec
        result = self.arms[arm_i].pick()
        # set result
        self.counts[arm_i] += 1
        self.rewards[arm_i] += result

    def exec(self):
        for i in range(self.n):
            if i % 100 == 0:
                self.e /= 2
            self.exec_one()
        mus = [arm.mu for arm in self.arms]
        print('counts: ', self.counts)
        print('mus: ', mus)
        print('search N: ', self.search_n)
        print('total reward: ', sum(self.rewards))

eg = EGreedy(4, 100000, 0.6)
eg.exec()

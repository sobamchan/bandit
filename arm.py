import random

class Arm(object):

    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def pick(self):
        return random.gauss(self.mu, self.sigma)

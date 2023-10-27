import math
import random

from algorithm.SA import SimulatedAnnealing, Space, Disturbance, TargetFunction


class Target(TargetFunction):
    def __call__(self, x):
        return (x - 3) ** 2


class NearSample(Disturbance):
    def __call__(self, x, temperature=None):
        return x + math.log(temperature + 1, 10) * (random.random() - 0.5)


class SampleSpace(Space):
    def sample(self):
        return 0


if __name__ == "__main__":
    sa = SimulatedAnnealing(1000, 0.00001, 0.999, NearSample())
    x, y = (sa.optimize(Target(), SampleSpace()))
    print(x, y)




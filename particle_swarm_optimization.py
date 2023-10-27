import math
import random

import numpy as np

from algorithm.PSO import ParticleSwarmOptimization
from algorithm.templates import Space, TargetFunction


class SpeedSpace(Space):
    def sample(self):
        return np.array([1, 1, 1, 1]).astype(np.float128)


class SampleSpace(Space):
    def sample(self):
        return np.random.rand(4).astype(np.float128)


class Target(TargetFunction):
    def __call__(self, x):
        return np.sum(np.square(x - 3) + x[0] - x[1] + np.square(x[2] - x[3]))


if __name__ == "__main__":
    pso = ParticleSwarmOptimization(50, 1000, SpeedSpace(), copy_function=np.ndarray.copy)
    x, y = pso.optimize(Target(), SampleSpace())
    print(x, y)

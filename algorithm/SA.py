# simulated Annealing
import math
import random

from algorithm.templates import Optimizer, TargetFunction, Space, Disturbance


class SimulatedAnnealing(Optimizer):
    def __init__(self, init_temperature: float, end_temperature: float, decay: float, disturbance: Disturbance):
        self.temperature = init_temperature
        self.end_temperature = end_temperature
        self.decay = decay
        self.disturb = disturbance

    def optimize(self, target_function: TargetFunction, x_space: Space):
        best_x = None
        best_y = float("inf")
        x_iter = x_space.sample()
        y = target_function(x_iter)

        while self.temperature > self.end_temperature:
            x_next = self.disturb(x_iter, self.temperature)
            y_next = target_function(x_next)
            if y_next < y or random.random() < math.exp(-(y_next - y) / self.temperature):
                x_iter, y = x_next, y_next
                if y < best_y:
                    best_x, best_y = x_iter, y

            self.temperature *= self.decay

        return best_x, best_y

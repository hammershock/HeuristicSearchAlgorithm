import heapq
import random

from templates import Space, TargetFunction, Optimizer


class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = None

    def calculate(self, target_function):
        self.fitness = target_function(self.chromosome)
        return self

    def crossover(self, other: 'Individual') -> 'Individual':
        cut_point = random.randint(0, len(self.chromosome) - 1)
        return Individual(self.chromosome[:cut_point] + other.chromosome[cut_point:])

    def mutate(self) -> 'Individual':
        random_bit = random.randint(0, len(self.chromosome) - 1)
        self.chromosome[random_bit] = 1 - self.chromosome[random_bit]  # bit inverse
        return self

    def __lt__(self, other: 'Individual'):
        return self.fitness < other.fitness


class GeneticAlgorithm(Optimizer):
    def __init__(self, population_size, num_iteration, num_select, num_elite, mutation_rate):
        self.population_size = population_size
        self.num_iteration = num_iteration
        self.num_select = num_select
        self.num_elite = num_elite
        self.mutation_rate = mutation_rate

    def optimize(self, target_function: TargetFunction, x_space: Space):
        population = [Individual(x_space.sample()).calculate(target_function) for _ in range(self.population_size)]
        best_individual = None
        combinations = [(i, j) for i in range(self.num_select) for j in range(i)]

        for _ in range(self.num_iteration):
            selected = []
            m = heapq.nsmallest(self.num_select, population)
            best_individual = m[0]
            selected += m[:self.num_elite]

            for idx1, idx2 in random.sample(combinations, k=self.population_size - self.num_elite):
                selected.append(m[idx1].crossover(m[idx2]).calculate(target_function))

            for individual in selected[self.num_elite:]:
                if random.random() < self.mutation_rate:
                    individual.mutate()

            population = selected
        return best_individual.chromosome, best_individual.fitness


class Function(TargetFunction):
    def __call__(self, chromosome):
        return sum(chromosome)


class SampleSpace(Space):
    def sample(self):
        return [random.randint(0, 1) for _ in range(100)]


if __name__ == "__main__":
    ga = GeneticAlgorithm(100, 500, 50, 5, 0.001)
    x, y = ga.optimize(Function(), SampleSpace())
    print(x)
    print(y)

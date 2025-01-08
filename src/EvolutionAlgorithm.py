from Magazine import Magazine
from Chromosome import Chromosome
from typing import List, Tuple, Dict
from random import choice, sample, random
from copy import deepcopy
import numpy as np


class EvolutionAlgorithm:
    def __init__(self, vertices: List[Tuple[int, int]],
                        wares_data: List[Tuple[int, int]],
                        population_size: int,
                        tournament_size: int,
                        selection_func,
                        elite_size: int,
                        mutation_rate: float,
                        mutation_weights: List[float],
                        crossover_rate: float,
                        crossover_func,
                        episodes: int,
                        eval_func_factors: List,
                        name: str):
        self.crossover_func = crossover_func
        self.selection_func = selection_func
        self.eval_func_factors = eval_func_factors
        self.magazine = Magazine(vertices=vertices)
        self.population_size = population_size
        self.wares_data = wares_data
        self.chromosomes = [Chromosome(wares=wares, matrix_shape=self.magazine.matrix.shape) for wares in
                            [self.magazine.generate_magazine_wares(wares_data=wares_data) for _ in range(self.population_size)]]
        self.elite_size = elite_size
        self.tournament_size = tournament_size
        self.mutation_rate = mutation_rate
        self.mutation_weights = mutation_weights
        self.crossover_rate = crossover_rate
        self.episodes = episodes
        self.name = name

    def _evaluate_chromosome(self, chromosome: Chromosome):
        new_matrix, filled_space, collisions, wall_collisions, something_nearby = self.magazine.fill_magazine_with_wares(wares=chromosome.wares)
        chromosome.matrix = new_matrix
        value = (self.eval_func_factors[0]*filled_space -
                 self.eval_func_factors[1]*wall_collisions -
                 self.eval_func_factors[2]*collisions -
                 self.eval_func_factors[3]*something_nearby)
        return value

    def _mutate(self):
        elites = deepcopy(self._get_best())
        for chromosome in self.chromosomes:
            chromosome.mutate(self.mutation_rate, self.mutation_weights)
        self.chromosomes += elites

    def _get_best(self, chromosomes: List[Chromosome] = None):
        if chromosomes is None:
            chromosomes = self.chromosomes
        chromosomes.sort(key=self._evaluate_chromosome, reverse=True)
        return chromosomes[:self.elite_size]

    def _tournament_selection(self):
        chosen_ones = deepcopy(self._get_best())
        for _ in range(self.population_size - self.elite_size):
            fighters = sample(self.chromosomes, self.tournament_size)
            winner = max(fighters, key=self._evaluate_chromosome)
            chosen_ones.append(winner)
        self.chromosomes = chosen_ones

    def _roulette_selection(self):
        fitness_values = np.array([self._evaluate_chromosome(chromosome) for chromosome in self.chromosomes])

        min_fitness = fitness_values.min()
        if min_fitness < 0:
            fitness_values -= min_fitness
        total_fitness = fitness_values.sum()
        if total_fitness == 0:
            probabilities = np.full(len(fitness_values), 1 / len(fitness_values))
        else:
            probabilities = fitness_values / total_fitness

        selected_indices = np.random.choice(
            len(self.chromosomes),
            size=self.population_size - self.elite_size,
            replace=True,
            p=probabilities
        )

        new_population = deepcopy(self._get_best())

        for idx in selected_indices:
            new_population.append(deepcopy(self.chromosomes[idx]))

        self.chromosomes = new_population

    def _reproduce(self, crossover_func):
        new_population = deepcopy(self._get_best())
        while len(new_population) < self.population_size:
            parent1, parent2 = sample(self.chromosomes, 2)
            if random() < self.crossover_rate:
                new_population.append(crossover_func(parent1, parent2))
            else:
                new_population.append(choice([parent1, parent2]))
        self.chromosomes = new_population

    def _mutate_best(self, count: int = 300, stagnate: int = 0):
        new_count = int(count*(1.1**stagnate))
        best = self._get_best()[0]
        to_mutate = [deepcopy(best) for _ in range(new_count)]
        for _ in range(5):
            for chromosome in to_mutate:
                chromosome.mutate(0.8, self.mutation_weights)
        best_mutated = self._get_best(to_mutate)[0]
        self.chromosomes.append(best_mutated)

    def _get_population_avg_quality(self):
        value = sum(self._evaluate_chromosome(chromosome) for chromosome in self.chromosomes)
        return value/self.population_size


    def run(self, verbose=False):
        stagnate = 0
        previous_best = float('-inf')
        count = int(0.1*self.population_size)
        best_dict = {}
        avg_quality_dict = {}
        for i in range(self.episodes+1):
            if verbose: print(f'Episode {i}')

            self._reproduce(self.crossover_func)
            self._mutate()
            self.selection_func(self)

            best_chromosome = self._get_best()[0]
            best_score = self._evaluate_chromosome(best_chromosome)
            best_dict[i] = best_score
            avg_quality_dict[i] = self._get_population_avg_quality()

            if verbose: print(f'Best_score: {best_score}')

            if best_score > previous_best:
                stagnate = 0
            else:
                stagnate += 1
            self._mutate_best(count, stagnate)
            previous_best = best_score

            if i % 5 == 0:
                self.magazine.save_magazine_to_image(matrix=best_chromosome.matrix, wares=best_chromosome.wares,
                                                        filename=f'output/{self.name}/{i}.png')
            if stagnate == 20:
                break

        best_chromosome = self._get_best()[0]
        self.magazine.save_magazine_to_image(matrix=best_chromosome.matrix, wares=best_chromosome.wares,
                                             filename=f'output/{self.name}/last.png')
        return best_dict, avg_quality_dict

    @staticmethod
    def single_point_crossover(parent1, parent2):
        return parent1.crossover_one_point(parent2)

    @staticmethod
    def two_point_crossover(parent1, parent2):
        return parent1.crossover_two_point(parent2)


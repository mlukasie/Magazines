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
                        elite_size: int,
                        mutation_rate: float,
                        mutation_weights: List[float],
                        crossover_rate: float,
                        episodes: int,
                        eval_func_factors: List,
                        name: str):
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

    def evaluate_chromosome(self, chromosome: Chromosome):
        new_matrix, filled_space, collisions, wall_collisions, something_nearby = self.magazine.fill_magazine_with_wares(wares=chromosome.wares)
        chromosome.matrix = new_matrix
        value = (self.eval_func_factors[0]*filled_space -
                 self.eval_func_factors[1]*wall_collisions -
                 self.eval_func_factors[2]*collisions -
                 self.eval_func_factors[3]*something_nearby)
        return value

    def mutate(self):
        elites = deepcopy(self._get_best())
        for chromosome in self.chromosomes:
            chromosome.mutate(self.mutation_rate, self.mutation_weights)
        self.chromosomes += elites

    def _get_best(self):
        self.chromosomes.sort(key=self.evaluate_chromosome, reverse=True)
        return self.chromosomes[:self.elite_size]


    def tournament_selection(self):
        chosen_ones = deepcopy(self._get_best())
        for _ in range(self.population_size - self.elite_size):
            fighters = sample(self.chromosomes, self.tournament_size)
            winner = max(fighters, key=self.evaluate_chromosome)
            chosen_ones.append(winner)
        self.chromosomes = chosen_ones


    def reproduce(self):
        new_population = deepcopy(self._get_best())
        while len(new_population) < self.population_size:
            parent1, parent2 = sample(self.chromosomes, 2)
            if random() < self.crossover_rate:
                new_population.append(parent1.crossover(parent2))
            else:
                new_population.append(choice([parent1, parent2]))
        self.chromosomes = new_population

    def mutate_worst(self, count: int = 300, stagnate:int = 0):
        self.chromosomes.sort(key=self.evaluate_chromosome, reverse=False)
        new_count = int(count*(1.1**stagnate))
        print(f'Mutated worst: {new_count}')
        for _ in range(5):
            for chromosome in self.chromosomes[:new_count]:
                chromosome.mutate(0.8, self.mutation_weights)


    def run(self):
        stagnate = 0
        previous_best = float('-inf')
        for i in range(self.episodes+1):
            print(f'Episode {i}')
            self.reproduce()
            self.mutate()
            self.tournament_selection()
            best_chromosome = self._get_best()[0]
            best_score = self.evaluate_chromosome(best_chromosome)
            print(f'Best_score: {best_score}')
            if best_score > previous_best:
                stagnate = 0
            else:
                stagnate += 1
            self.mutate_worst(300, stagnate)
            previous_best = best_score
            if i % 5 == 0:
                self.magazine.save_magazine_to_image(matrix=best_chromosome.matrix, wares=best_chromosome.wares,
                                                        filename=f'output/{self.name}/{i}.png')
            if stagnate >= 20:
                break
        best_chromosome = self._get_best()[0]
        best_score = self.evaluate_chromosome(best_chromosome)
        print(f'Best_score: {best_score}')
        self.magazine.save_magazine_to_image(matrix=best_chromosome.matrix, wares=best_chromosome.wares,
                                             filename=f'output/{self.name}/last.png')





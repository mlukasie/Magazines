from Magazine import Magazine
from Chromosome import Chromosome
from typing import List, Tuple
from random import choice, sample, random
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
                        episodes: int):
        self.magazine = Magazine(vertices=vertices)
        self.population_size = population_size
        self.chromosomes = [Chromosome(wares=wares, matrix_shape=self.magazine.matrix.shape) for wares in
                            [self.magazine.generate_magazine_wares(wares_data=wares_data) for _ in range(self.population_size)]]
        self.elite_size = elite_size
        self.elites = self.get_best()
        self.tournament_size = tournament_size
        self.mutation_rate = mutation_rate
        self.mutation_weights = mutation_weights
        self.crossover_rate = crossover_rate
        self.episodes = episodes

    def evaluate_chromosome(self, chromosome: Chromosome):
        new_matrix, filled_space, collisions, wall_collisions, something_nearby = self.magazine.fill_magazine_with_wares(wares=chromosome.wares)
        chromosome.matrix = new_matrix
        value = filled_space - 10*wall_collisions - 10*collisions - 2*something_nearby
        return value

    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate(self.mutation_rate, self.mutation_weights)

    def get_best(self):
        self.chromosomes.sort(key=self.evaluate_chromosome, reverse=True)
        return self.chromosomes[:self.elite_size]

    def tournament_selection(self):
        chosen_ones = self.elites.copy()
        for _ in range(self.population_size - self.elite_size):
            fighters = sample(self.chromosomes, self.tournament_size)
            winner = max(fighters, key=self.evaluate_chromosome)
            chosen_ones.append(winner)
        self.elites = self.get_best()
        self.chromosomes = chosen_ones

    def reproduce(self):
        new_population = self.elites.copy()
        while len(new_population) < self.population_size:
            parent1, parent2 = sample(self.chromosomes, 2)
            if random() < self.crossover_rate:
                new_population.append(parent1.crossover(parent2))
            else:
                new_population.append(choice([parent1, parent2]))
        self.elites = self.get_best()
        self.chromosomes = new_population

    def run(self):
        for i in range(self.episodes):
            print(f'Episode {i} '
                  f'Best result: {self.evaluate_chromosome(self.elites[0])}')
            self.mutate()
            print('turnament')
            self.tournament_selection()
            print('reproduction')
            self.reproduce()
            self.magazine.save_magazine_to_image(matrix=self.elites[0].matrix, wares=self.elites[0].wares, filename=f'output/{i}.png')


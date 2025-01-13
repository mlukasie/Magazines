from Ware import Ware
from Enums import MutationType as MT, Orientation
from typing import List
from random import random, randint, choices, choice



class Chromosome:
    def __init__(self, wares: List[Ware], matrix_shape):
        self.wares = wares
        self.matrix = None
        self.matrix_shape = matrix_shape

    def mutate(self, probability: float, weights: List[float]) -> None:
        if random() < probability:
            iteration = randint(0, len(self.wares) - 1)
            ware = self.wares[iteration]
            mutation_type = choices([MT.POSITION_X, MT.POSITION_Y, MT.ORIENTATION, MT.EXISTENCE], weights=weights)[0]
            if mutation_type == MT.POSITION_X:
                x = ware.x
                if x == 0:
                    x = 1
                elif x == (self.matrix_shape[0]-1):
                    x = self.matrix_shape[0]-2
                else:
                    x = x + choice([1, -1])
                ware.x = x
            elif mutation_type == MT.POSITION_Y:
                y = ware.y
                if y == 0:
                    y = 1
                elif y == (self.matrix_shape[1] - 1):
                    y = self.matrix_shape[1] - 2
                else:
                    y = y + choice([1, -1])
                ware.y = y
            elif mutation_type == MT.ORIENTATION:
                orientation = ware.orientation
                orientation = Orientation.VERTICAL if orientation == Orientation.HORIZONTAL else Orientation.HORIZONTAL
                ware.orientation = orientation
            elif mutation_type == MT.EXISTENCE:
                existence = ware.is_present
                existence = False if existence else True
                ware.is_present = existence

    def crossover_one_point(self, other: 'Chromosome') -> 'Chromosome':
        """One-point crossover"""
        cross_point = randint(1, len(self.wares) - 1)
        child1 = Chromosome(self.wares[0:cross_point] + other.wares[cross_point:], matrix_shape=self.matrix_shape)
        child2 = Chromosome(other.wares[0:cross_point] + self.wares[cross_point:], matrix_shape=self.matrix_shape)
        return choice([child1, child2])


    def crossover_two_point(self, other: 'Chromosome') -> 'Chromosome':
        """Two-point crossover."""
        point1 = randint(0, len(self.wares) - 2)
        point2 = randint(point1 + 1, len(self.wares) - 1)

        child_wares1 = (
                self.wares[:point1] +
                other.wares[point1:point2 + 1] +
                self.wares[point2 + 1:]
        )
        child_wares2 = (
                other.wares[:point1] +
                self.wares[point1:point2 + 1] +
                other.wares[point2 + 1:]
        )

        return Chromosome(wares=choice([child_wares1, child_wares2]), matrix_shape=self.matrix_shape)





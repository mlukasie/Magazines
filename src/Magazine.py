import numpy as np
from shapely.geometry import Polygon, Point
from typing import List, Tuple
from random import randint, choice

from Ware import Ware
from MagazineWare import MagazineWare, Orientation
from Enums import Orientation, FieldStatus


class Magazine:
    def __init__(self, vertices: List[Tuple[int, int]]):
        self.matrix: np.ndarray = self._generate_matrix(vertices=vertices)

    @staticmethod
    def _generate_matrix(vertices: List[Tuple[int, int]]) -> np.ndarray:
        """
        Generates matrix based on given vertices.
        It represents empty magazine.
        Vertices should be in order that enables drawing polygon without
        taking your hand off
        :param vertices:
        """
        polygon = Polygon(vertices)

        width = max([vertex[0] for vertex in vertices]) + 1
        length = max([vertex[1] for vertex in vertices]) + 1

        grid_size = (width, length)
        matrix = np.full(grid_size, fill_value=FieldStatus.WALL, dtype=FieldStatus)

        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                if polygon.covers(Point(x, y)):
                    matrix[x, y] = FieldStatus.EMPTY
        return matrix

    def generate_magazine_wares(self, wares: List[Ware]) -> List[MagazineWare]:
        """
        Randomly choose attributes for given Wares
        Much likely to give result with wares on top of each other or colliding with walls
        :param wares:
        """
        matrix_length = len(self.matrix)
        matrix_width = len(self.matrix[0])
        magazine_wares: List[MagazineWare] = []
        for ware in wares:
            magazine_wares.append(MagazineWare(ware=ware,
                                               x=randint(0, matrix_length - 1),
                                               y=randint(0, matrix_width - 1),
                                               orientation=choice([Orientation.VERTICAL, Orientation.HORIZONTAL]),
                                               is_present=choice([True, False])))
        return magazine_wares



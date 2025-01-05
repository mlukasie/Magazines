import numpy as np
from Ware import Ware
from MagazineWare import MagazineWare, Orientation
from typing import List
from random import randint, choice


class Magazine:
    def __init__(self, matrix: np.ndarray):
        self.matrix = matrix

    def generateMagazineWares(self, wares: List[Ware]) -> List[MagazineWare]:
        """
        Randomly choose attributes for given Wares
        Much likely to give result with wares on top of each other or colliding with walls
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



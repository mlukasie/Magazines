import numpy as np
from shapely.geometry import Polygon, Point
from typing import List, Tuple
from random import randint, choice
import pygame

from Ware import Ware
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

    def generate_magazine_wares(self, wares_data: List[Tuple[int, int]]) -> List[Ware]:
        """
        Randomly choose attributes for given Wares
        Much likely to give result with wares on top of each other or colliding with walls.
        :param wares_data:
        """
        matrix_length = len(self.matrix)
        matrix_width = len(self.matrix[0])
        magazine_wares: List[Ware] = []
        for ware in wares_data:
            magazine_wares.append(Ware(height = ware[0],
                                       width = ware[1],
                                       x=randint(0, matrix_length - 1),
                                       y=randint(0, matrix_width - 1),
                                       orientation=choice([Orientation.VERTICAL, Orientation.HORIZONTAL]),
                                       is_present=choice([True, False])))
        return magazine_wares

    @staticmethod
    def show_magazine(matrix: np.ndarray[FieldStatus], wares: List[Ware] = None) -> None:
        pygame.init()

        max_size = 500
        rows, cols = matrix.shape
        cell_size = min(max_size // cols, max_size // rows)
        width, height = cols * cell_size, rows * cell_size

        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Magazine")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for row in range(rows):
                for col in range(cols):
                    color = matrix[row, col].value
                    pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
            if wares is not None:
                for ware in wares:
                    x_pos = ware.x * cell_size
                    y_pos = ware.y * cell_size
                    ware_width = ware.width * cell_size
                    ware_height = ware.height * cell_size
                    if ware.orientation == Orientation.HORIZONTAL:
                        ware_width, ware_height = ware_height, ware_width
                    pygame.draw.rect(screen, (0, 0, 0), (y_pos, x_pos, ware_width, ware_height), 3)
            pygame.display.flip()

        pygame.quit()

    def fill_magazine_with_wares(self, wares: List[Ware]) -> (np.ndarray, int, int):
        """
        Place provided wares in matrix.
        Returns few things:
        Copy of magazine matrix with applied wares on it.
        Number of collisions with walls.
        Number of collisions with wares
        :param wares:
        :return:
        """
        new_matrix = self.matrix.copy()
        collisions = 0
        wall_collisions = 0
        rows, cols = new_matrix.shape
        for ware in wares:
            width = ware.width
            height = ware.height
            if ware.orientation == Orientation.HORIZONTAL:
                width, height = height, width
            for i in range(height):
                for j in range(width):
                    x, y = ware.x + i, ware.y + j
                    if 0 <= x < rows and 0 <= y < cols:
                        field = new_matrix[x, y]
                    else:
                        wall_collisions += 1
                        continue
                    if field == FieldStatus.EMPTY:
                        new_matrix[ware.x + i, ware.y + j] = FieldStatus.WARE
                    elif field == FieldStatus.WALL:
                        new_matrix[ware.x + i, ware.y + j] = FieldStatus.WALL_COLLISION
                        wall_collisions += 1
                    elif field == FieldStatus.WARE:
                        new_matrix[ware.x + i, ware.y + j] = FieldStatus.COLLISION
                        collisions += 1
                    elif field == FieldStatus.COLLISION:
                        collisions += 1
                    elif field == FieldStatus.WALL_COLLISION:
                        wall_collisions += 1

        return new_matrix, collisions, wall_collisions

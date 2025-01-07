import numpy as np
from shapely.geometry import Polygon, Point
from typing import List, Tuple
from random import randint, choice, choices
import pygame
from copy import deepcopy
from os import path, makedirs

from Ware import Ware
from Enums import Orientation, FieldStatus


class Magazine:
    def __init__(self, vertices: List[Tuple[int, int]]):
        self.matrix, self.size = self._generate_matrix(vertices=vertices)

    @staticmethod
    def _generate_matrix(vertices: List[Tuple[int, int]]) -> np.ndarray:
        """
        Generates matrix based on given vertices.
        It represents empty magazine.
        Vertices should be in order that enables drawing polygon without
        taking your hand off.
        """
        polygon = Polygon(vertices)

        width = max([vertex[0] for vertex in vertices]) + 1
        length = max([vertex[1] for vertex in vertices]) + 1

        grid_size = (width, length)
        matrix = np.empty(grid_size, dtype=object)
        size = 0
        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                if polygon.covers(Point(x, y)):
                    matrix[x, y] = (FieldStatus.EMPTY, [])
                    size = size + 1
                else:
                    matrix[x, y] = (FieldStatus.WALL, [-1])
        return matrix, size

    def generate_magazine_wares(self, wares_data: List[Tuple[int, int]]) -> List[Ware]:
        """
        Randomly choose attributes for given Wares.
        """
        matrix_length = len(self.matrix)
        matrix_width = len(self.matrix[0])
        magazine_wares: List[Ware] = []
        for ware_id, ware_data in enumerate(wares_data, start=1):
            magazine_wares.append(Ware(height=ware_data[0],
                                       width=ware_data[1],
                                       x=randint(0, matrix_length - 1),
                                       y=randint(0, matrix_width - 1),
                                       orientation=choice([Orientation.VERTICAL, Orientation.HORIZONTAL]),
                                       is_present=choices([True, False], weights=[60, 40])[0],
                                       id=ware_id))
        return magazine_wares

    @staticmethod
    def save_magazine_to_image(matrix: np.ndarray, wares: List[Ware] = None, filename: str = "magazine.png") -> None:
        directory = path.dirname(filename)
        if directory and not path.exists(directory):
            makedirs(directory)
        pygame.init()

        max_size = 500
        rows, cols = matrix.shape
        cell_size = min(max_size // cols, max_size // rows)
        width, height = cols * cell_size, rows * cell_size

        surface = pygame.Surface((width, height))

        for row in range(rows):
            for col in range(cols):
                field_status, ids = matrix[row, col]
                color = field_status.value
                pygame.draw.rect(surface, color, (col * cell_size, row * cell_size, cell_size, cell_size))

        if wares is not None:
            for ware in wares:
                if not ware.is_present:
                    continue
                x_pos = ware.x * cell_size
                y_pos = ware.y * cell_size
                ware_width = ware.width * cell_size
                ware_height = ware.height * cell_size
                if ware.orientation == Orientation.HORIZONTAL:
                    ware_width, ware_height = ware_height, ware_width
                pygame.draw.rect(surface, (0, 0, 0), (y_pos, x_pos, ware_width, ware_height), 3)

        pygame.image.save(surface, filename)

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
        new_matrix = deepcopy(self.matrix)
        collisions = 0
        wall_collisions = 0
        something_nearby = 0
        filled_space = 0
        rows, cols = new_matrix.shape
        for ware in wares:
            if not ware.is_present:
                continue
            width = ware.width
            height = ware.height
            if ware.orientation == Orientation.HORIZONTAL:
                width, height = height, width
            for i in range(height):
                for j in range(width):
                    x, y = ware.x + i, ware.y + j
                    if 0 <= x < rows and 0 <= y < cols:
                        field_status, ids = new_matrix[x, y]
                    else:
                        wall_collisions += 1
                        continue
                    if field_status == FieldStatus.EMPTY:
                        new_matrix[x, y] = (FieldStatus.WARE, ids + [ware.id])
                    elif field_status == FieldStatus.WALL:
                        new_matrix[x, y] = (FieldStatus.WALL_COLLISION, ids + [ware.id])
                        wall_collisions += 1
                    elif field_status == FieldStatus.WARE:
                        new_matrix[x, y] = (FieldStatus.COLLISION, ids + [ware.id])
                        collisions += 1
                    elif field_status == FieldStatus.COLLISION:
                        new_matrix[x, y] = (FieldStatus.COLLISION, ids + [ware.id])
                        collisions += 1
                    elif field_status == FieldStatus.WALL_COLLISION:
                        new_matrix[x, y] = (FieldStatus.WALL_COLLISION, ids + [ware.id])
                        wall_collisions += 1
        for x in range(rows):
            for y in range(cols):
                neighbors_cords = self._get_neighbours(x, y)
                field_status, ids = new_matrix[x, y]
                if field_status == FieldStatus.WARE or field_status == FieldStatus.COLLISION:
                    filled_space += 1
                    something_nearby += (8 - len(neighbors_cords))
                    for neighbor_cord in neighbors_cords:
                        neighbor_field_status, neighbor_ids = new_matrix[neighbor_cord[0], neighbor_cord[1]]
                        new_ids = set(neighbor_ids) - set(ids)
                        something_nearby += len(new_ids)

        return new_matrix, filled_space, collisions, wall_collisions, something_nearby

    def _get_neighbours(self, pos_x, pos_y) -> List[Tuple[int, int]]:
        cords = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        neighbors_cords = [(pos_x + cord[0], pos_y + cord[1]) for cord in cords]
        to_remove = []
        for cord in neighbors_cords:
            x, y = cord
            if (x < 0 or y < 0) or (x >= self.matrix.shape[0] or y >= self.matrix.shape[1]):
                to_remove.append(cord)
        for cord in to_remove:
            neighbors_cords.remove(cord)
        return neighbors_cords

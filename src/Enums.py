from enum import Enum


class FieldStatus(Enum):
    EMPTY = 'EMPTY'
    WALL = 'WALL'
    COLLISION = 'COLLISION'


class Orientation(Enum):
    VERTICAL = 'VERTICAL'
    HORIZONTAL = 'HORIZONTAL'

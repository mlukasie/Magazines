from enum import Enum, auto


class FieldStatus(Enum):
    EMPTY = (255, 255, 255)  # White
    WALL = (0, 0, 0)  # Black
    WALL_COLLISION = (255, 0, 0)  # Red
    WARE = (0, 255, 0)  # Green
    COLLISION = (255, 165, 0)  # Orange


class Orientation(Enum):
    VERTICAL = auto()
    HORIZONTAL = auto()


class MutationType(Enum):
    ORIENTATION = auto()
    EXISTENCE = auto()
    POSITION_X = auto()
    POSITION_Y = auto()

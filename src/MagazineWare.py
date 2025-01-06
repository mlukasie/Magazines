from Ware import Ware
from Enums import Orientation


class MagazineWare:
    def __init__(self, ware: Ware, x: int, y: int, orientation: Orientation, is_present: bool) -> None:
        self.ware = ware
        self.x = x
        self.y = y
        self.orientation = orientation
        self.is_present = is_present

    def __str__(self) -> str:
        return (f'MagazineWare: ({self.ware} x: {self.x} '
                f'y: {self.y}) orientation: {self.orientation} '
                f'present: {self.is_present})')

from Enums import Orientation


class Ware:
    def __init__(self, height: int, width: int, x: int, y: int, orientation: Orientation, is_present: bool) -> None:
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.orientation = orientation
        self.is_present = is_present

    def __str__(self) -> str:
        return (f'MagazineWare( height: {self.height} width: {self.width} '
                f'x: {self.x} y: {self.y}) orientation: {self.orientation} '
                f'present: {self.is_present})')

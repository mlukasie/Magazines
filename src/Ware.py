class Ware:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __str__(self) -> str:
        return f'Length:{self.length} Width:{self.width}'

class Ware:
    def __init__(self, id: int, length: int, width: int):
        self.id = id
        self.length = length
        self.width = width

    def __str__(self) -> str:
        return f'Id:{self.id} Length:{self.length} Width:{self.width}'
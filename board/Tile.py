class Tile:
    index: int

    def __init__(self, i: int):
        self.index = i

    def __str__(self):
        return str(self.index)

from random import randint

default = [{
    "id": 0,
    "name": "Puente",
    "description": ""
}, {
    "id": 1,
    "name": "Resbalon",
    "description": ""
}, {
    "id": 2,
    "name": "Calavera",
    "description": ""
}]


class Tile:
    def __init__(self, i: int):
        self.index = i

        self.punishments = default

    def __str__(self):
        return str(self.index)

    def getPunish(self, currentTile: int) -> int:
        if len(self.punishments) == 0:
            self.punishments = default

        punishment = self.punishments[randint(0, len(self.punishments) - 1)]
        
        if punishment["id"] == 0:
            pass
        elif punishment["id"] == 1:
            pass
        else:
            pass

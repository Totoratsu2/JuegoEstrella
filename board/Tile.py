from typing import TypedDict

from random import randint
from utils import clearConsole

default = [{
    "id": 0,
    "name": "Puente",
    "description": "El jugador retrocede 3 casillas"
}, {
    "id": 1,
    "name": "Resbalon",
    "description": "El jugador retrocede 2 casillas"
}, {
    "id": 2,
    "name": "Calavera",
    "description": "El jugador vuelve a la casilla 0"
}]


def _printPunishment(punishment: list[TypedDict]):
    clearConsole()

    lines = "\t" + ("---" * 10) + "-----"
    name = punishment["name"]
    desc = punishment["description"]

    print("\n\n" + lines)
    print(f"\t|\t {name} \t\t|\n{lines}\n\t| {desc} |\n{lines}\n\n")


def getPunish(currentTile: int) -> int:
    punishment = default[randint(0, len(default) - 1)]

    if punishment["id"] == 0:
        _printPunishment(punishment)
        return -3
    elif punishment["id"] == 1:
        _printPunishment(punishment)
        return -2
    else:
        _printPunishment(punishment)
        return (currentTile) * -1


class Tile:
    def __init__(self, i: int):
        self.index = i

        self.punishments = default

    def __str__(self):
        return str(self.index)

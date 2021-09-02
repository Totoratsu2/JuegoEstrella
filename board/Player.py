from colorama import Style
from board.Tile import Tile

class Player:
    def __init__(self, color: str):
        self.color = color
        self.score = 0

        self.tilePosition = 0

    def __str__(self):
        return f"{self.color}★{Style.RESET_ALL}"

    def turn(self, index: int) -> str:
        return f"{self.color}{index}{Style.RESET_ALL}"

    def isInCoords(self, tile: int) -> bool:
        if self.tilePosition == tile:
            return True
        return False

    def goTo(self, tile: int, lenght: list[int]) -> bool:
        totalLenght = (lenght[0] * lenght[1]) - 1

        if (self.tilePosition + tile) < 0:
            self.tilePosition = 0
        elif (self.tilePosition + tile) > totalLenght:
            self.tilePosition = totalLenght
            return True
        else:
            self.tilePosition += tile
            if  self.tilePosition >= totalLenght:
                return True

        return False
from colorama import Style


class Player:
    tilePosition = 0
    score = 0
    color: str

    def __init__(self, color: str):
        self.color = color

    def __str__(self):
        return f"{self.color}★{Style.RESET_ALL}"

    def turn(self, index: int) -> str:
        return f"{self.color}{index}{Style.RESET_ALL}"

    def isInCoords(self, tile: int) -> bool:
        if self.tilePosition == tile:
            return True
        return False
from colorama.ansi import Fore, Style
from board.Tile import Tile
from board.Player import Player

from questions.main import getQuestions


class Board:
    lenght: list[int]
    tiles: list[list[Tile]]

    currentTurn = 0
    dice = 0

    player1: Player
    player2: Player

    def __init__(self, n=1, m=5):
        self.lenght = [n, m]

        self.player1 = Player(Fore.BLUE)
        self.player2 = Player(Fore.RED)

        self.generate()

    def generate(self) -> None:
        questions = getQuestions()
        matrix: list[list[Tile]] = []
        count = 0

        for _ in range(self.lenght[1]):
            temp: list[Tile] = []

            for __ in range(self.lenght[0]):
                temp.append(Tile(count))
                count += 1

            matrix.append(temp)

        self.tiles = matrix

    def _getTurn(self) -> str:
        if (self.currentTurn % 2 == 0):
            return self.player1.turn(1)
        return self.player2.turn(2)

    def _showTurnAndDice(self):
        topTableLines = "\t" + ("-----" * 10)

        print(topTableLines)
        print(
            f"\t|\tJugador en turno\t|\t {self._getTurn()}\t |\n{topTableLines}"
        )
        print(f"\t|\t\tDado\t\t|\t {self.dice}\t |\n{topTableLines}")

    def _showPlayerScoreBoard(self):
        lines = "\t" + ("----" * 4)
        matrix = [[
            f"\t| {self.player1.color}Jugador 1{Style.RESET_ALL} \t|",
            f"\t| {self.player2.color}Jugador 2{Style.RESET_ALL} \t|"
        ],
                  [
                      f"\t| Casilla  | {self.player1.tilePosition} \t|",
                      f"\t| Casilla  | {self.player2.tilePosition} \t|"
                  ],
                  [
                      f"\t| Aciertos | {self.player1.score} \t|",
                      f"\t| Aciertos | {self.player2.score} \t|"
                  ]]

        print(f"{lines}\t{lines}")
        for line in matrix:
            print("\t".join(line))
            print(f"{lines}\t{lines}")

    def show(self):
        boardLines = "-----" * self.lenght[0]
        tiles = [0, 0]

        self._showTurnAndDice()

        # Show board
        print(f"\t\t{boardLines}")
        for y in self.tiles:
            row = ''
            for x in y:
                tile = ''
                isP1 = self.player1.isInCoords(tiles[0])
                isP2 = self.player2.isInCoords(tiles[0])

                if not (isP1 or isP2):
                    tile = f" {x}" if x.index < 10 else f"{x}"
                else:
                    if isP1:
                        tile = f"{self.player1}"
                    if isP2:
                        tile = tile + f"{self.player2}" if len(
                            tile) > 0 else f" {self.player2}"

                row = row + f"| {tile} " if tiles[
                    1] % 2 == 1 else f"| {tile} " + row
                tiles[0] += 1

            print(f"\t\t{row}|\n\t\t{boardLines}")
            tiles[1] += 1

        self._showPlayerScoreBoard()

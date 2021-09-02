from utils import clearConsole, readInt, stopConsole
from board.Tile import Tile, getPunish
from board.Player import Player
from colorama.ansi import Fore, Style

from random import randint
from questions.main import getQuestions


class Board:
    def __init__(self, n=1, m=5):
        self.lenght = [n, m]
        self.tiles = []

        self.gameOver = False
        self.currentTurn = 0
        self.dice = 0

        self.player1 = Player(Fore.CYAN)
        self.player2 = Player(Fore.LIGHTMAGENTA_EX)

        self.questions = getQuestions()
        self.generate()

    def showWinner(self):
        lines = "\t" + ("----" * 8) + "-"
        clearConsole()

        if self.player1.tilePosition > self.player2.tilePosition:
            print(f"\n\n{lines}")
            print(
                f"\t| Ganador |\t{self.player1.color}Jugador 1{Style.RESET_ALL}\t|"
            )
            print(f"{lines}\n\n")
        else:
            print(f"\n\n{lines}")
            print(
                f"\t| Ganador |\t{self.player2.color}Jugador 2{Style.RESET_ALL}\t|"
            )
            print(f"{lines}\n\n")

        self._showPlayerScoreBoard()

    def generate(self) -> None:
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
        lines = "\t" + ("----" * 4) + "-"
        player1Tab = "\t" if self.player1.tilePosition < 10 else ""
        player2Tab = "\t" if self.player2.tilePosition < 10 else ""

        matrix = [
            [
                f"\t| {self.player1.color}Jugador 1{Style.RESET_ALL} \t|",
                f"\t| {self.player2.color}Jugador 2{Style.RESET_ALL} \t|"
            ],
            [
                f"\t| Casilla  | {self.player1.tilePosition} {player1Tab}|",
                f"\t| Casilla  | {self.player2.tilePosition} {player2Tab}|"
            ],
            [
                f"\t| Aciertos | {self.player1.score} \t|",
                f"\t| Aciertos | {self.player2.score} \t|"
            ]
        ]

        print(f"{lines}\t{lines}")
        for line in matrix:
            print("\t".join(line))
            print(f"{lines}\t{lines}")

    def _rollDice(self):
        self.dice = randint(1, 6)

        if self.currentTurn % 2 == 0:
            self.gameOver = self.player1.goTo(self.dice, self.lenght)
        else:
            self.gameOver = self.player2.goTo(self.dice, self.lenght)

    def _askQuestion(self):
        question = self.questions[randint(0, len(self.questions) - 1)]
        self.questions.remove(question)

        clearConsole()
        question.show()

        response = None
        while response is None:
            response = readInt()
        correct = question.verifyOption(response)

        if not correct:
            if self.currentTurn % 2 == 0:
                self.player1.goTo(getPunish(self.player1.tilePosition),
                                  self.lenght)
            else:
                self.player2.goTo(getPunish(self.player2.tilePosition),
                                  self.lenght)
        else:
            if self.currentTurn % 2 == 0:
                self.player1.score += 1
            else:
                self.player2.score += 1

            clearConsole()
            print(f"\n\n\t{Fore.GREEN}Correcto!!!{Style.RESET_ALL}\n\n")

        stopConsole()

    def playTurn(self):
        stopConsole()
        self._rollDice()

        self.show()
        stopConsole()
        self._askQuestion()

        self.currentTurn += 1
        self.show()

    def show(self):
        clearConsole()
        boardLines = "-----" * self.lenght[0] + "-"
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
                        space = " " if not isP2 else ""
                        tile = f"{self.player1}{space}"
                    if isP2:
                        tile = tile + f"{self.player2}" if len(
                            tile) > 0 else f" {self.player2}"

                row = row + f"| {tile} " if tiles[
                    1] % 2 == 1 else f"| {tile} " + row
                tiles[0] += 1

            print(f"\t\t{row}|\n\t\t{boardLines}")
            tiles[1] += 1

        self._showPlayerScoreBoard()

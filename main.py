from board.Board import Board
from utils import clearConsole, stopConsole


def main():
    while True:
        board = Board(5, 4)

        while not board.gameOver:
            clearConsole()
            board.show()
            board.playTurn()

        board.showWinner()
        stopConsole("Presiona enter para volver a jugar ...")


if __name__ == '__main__':
    main()
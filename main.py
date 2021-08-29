from utils import clearConsole
from board.Board import Board


def main():
    clearConsole()
    board = Board(5, 4)
    board.show()


if __name__ == '__main__':
    main()
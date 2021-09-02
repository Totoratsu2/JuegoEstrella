from board.Board import Board
from colorama.ansi import Fore, Style

from utils import clearConsole, stopConsole


def main():
    while True:
        board = Board(5, 4)

        while not board.gameOver:
            board.show()
            board.playTurn()

        board.showWinner()
        stopConsole("Presiona enter para volver a jugar ...")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n\n\t\t{Fore.GREEN}Hasta pronto!!{Style.RESET_ALL}\n\n")
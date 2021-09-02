import os
from colorama.ansi import Fore, Style


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def stopConsole(msg='Presiona Enter para continuar ...'):
    input("\n" + msg)


def readInt(msg="Ingrese la opcion correcta: ", range=[0, 2]) -> int:
    try:
        result = int(input(msg))

        if not (range[0] <= result <= range[1]):
            print(
                f"\n{Fore.RED}ERROR:{Style.RESET_ALL} El numero debe de estar en el rango {range}.\n"
            )
            return None
        
        return result
    except ValueError:
        print(
            f"\n{Fore.RED}ERROR:{Style.RESET_ALL} Dato ingresado no es un numero entero.\n"
        )
        return None

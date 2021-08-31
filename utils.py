import os


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def stopConsole(msg='Presiona Enter para continuar ...'):
    input(msg)
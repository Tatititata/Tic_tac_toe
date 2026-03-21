from enum import Enum

class Responce(Enum):
    NOT_VALID = 0
    PLAYER = 'O'
    SERVER = 'X'
    TIE = 3
    GAME = 4

TOP = '╔═══╦═══╦═══╗\n'
DIV = '╠═══╬═══╬═══╣\n'
BOT = '╚═══╩═══╩═══╝\n'
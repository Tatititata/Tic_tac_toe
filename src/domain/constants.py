from enum import Enum

class Responce(Enum):
    NOT_VALID = 0
    O_PLAYER = 'O'
    X_PLAYER = 'X'
    TIE = 3
    IN_PROGRESS = 4

TOP = '╔═══╦═══╦═══╗\n'
DIV = '╠═══╬═══╬═══╣\n'
BOT = '╚═══╩═══╩═══╝\n'
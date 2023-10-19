import board
from ideaboard import IdeaBoard
import time

ib = IdeaBoard()

sw = ib.DigitalIn(board.IO27)
pot = ib.AnalogIn(board.IO33)

while True:
    valor = sw.value
    valor_pot = pot.value
    if valor_pot > 30000:
        ib.pixel = (0,255,0)
    else:
        ib.pixel = (0,0,0)

print("hola")
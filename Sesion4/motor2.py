import board
from ideaboard import IdeaBoard
import time

ib = IdeaBoard()

sw = ib.DigitalIn(board.IO27)
pot = ib.AnalogIn(board.IO33)

ultimo = time.monotonic() # 100.0
while True:
    # pot = 0-65535 (16 bits)
    valor = pot.value
    velocidad = ib.map_range(valor, 0, 65535, -1.0, 1.0)
    ib.motor_1.throttle = velocidad
    if time.monotonic() - ultimo > 0.2:
        print(valor, velocidad)
        ultimo = time.monotonic()
    
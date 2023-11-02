import board
from ideaboard import IdeaBoard
import time

ib = IdeaBoard()

sw = ib.DigitalIn(board.IO27)

while True:
    if sw.value == False:
        ib.motor_1.throttle = 1.0
    else:
        ib.motor_1.throttle = 0.0
    
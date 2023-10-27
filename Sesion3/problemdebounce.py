# debounce
import board
from ideaboard import IdeaBoard
import time

ib = IdeaBoard()

sw = ib.DigitalIn(board.IO27)

toggle = 1

ultimo = time.monotonic()
while True:
    if sw.value == False:
        if toggle == 1:
            toggle = 0
        elif toggle == 0:
            toggle = 1
    
    if time.monotonic() - ultimo > 0.2:
        print(toggle)
        ultimo = time.monotonic()
    
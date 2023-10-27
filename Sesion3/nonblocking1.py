# non blocking 2

import board
from ideaboard import IdeaBoard
import time

ib = IdeaBoard()

ultimo = time.monotonic()
while True:
   if time.monotonic() - ultimo > 2.0:
       print("bang!")
       ultimo = time.monotonic()
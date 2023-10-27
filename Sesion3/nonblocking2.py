# non blocking 2

import board
from ideaboard import IdeaBoard
import time

ib = IdeaBoard()

ultimo = time.monotonic()
ultimo2 = time.monotonic()

while True:
   if time.monotonic() - ultimo > 2.0:
       print("bang!")
       ultimo = time.monotonic()
       
   if time.monotonic() - ultimo2 > 5.0:
       print("boom!")
       ultimo2 = time.monotonic()
       
    # codigo
# https://learn.adafruit.com/key-pad-matrix-scanning-in-circuitpython/keys-one-key-per-pin

import board
from ideaboard import IdeaBoard
import time
import keypad

ib = IdeaBoard()

estatus = 0

keys = keypad.Keys((board.IO27,), value_when_pressed=False)

while True:
    event = keys.events.get()
    if event:
        if event.pressed:
            if estatus == 0:
                estatus = 1
            elif estatus == 1:
                estatus = 0
    ib.pixel = (255*estatus, 0, 0)

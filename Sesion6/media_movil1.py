import board
from ideaboard import IdeaBoard
import time

ib = IdeaBoard()

pot = ib.AnalogIn(board.IO33)

datos = []
tamano_filtro = 5

ultimo = time.monotonic()
while True:
    valor = pot.value
    datos.append(valor)
    if len(datos) > tamano_filtro:
        datos.pop(0)
        media = sum(datos)/len(datos)
        if time.monotonic() - ultimo > 0.2:
            print(media)
            ultimo = time.monotonic()
import board
from ideaboard import IdeaBoard
import time

ib = IdeaBoard()

pot = ib.AnalogIn(board.IO33)

datos = []
tamano_filtro = 50

def filtro(lista, val):
    lista.append(val)
    if len(datos)> tamano_filtro:
        lista.pop(0)
        resultado = sum(datos)/len(datos)
        return resultado

ultimo = time.monotonic()
while True:
    valor = pot.value
    media = filtro(datos, valor)
    if time.monotonic() - ultimo > 0.2:
        print(media)
        ultimo = time.monotonic()
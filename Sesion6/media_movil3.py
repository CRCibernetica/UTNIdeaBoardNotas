import board
from ideaboard import IdeaBoard
import time

ib = IdeaBoard()

pot = ib.AnalogIn(board.IO33)

class Filtro:
    
    def __init__(self, tam_filtro):
        self.tam_filtro = tam_filtro
        self.datos = []
        
    def agregar(self, val):
        self.datos.append(val)
        if len(self.datos) > self.tam_filtro:
            self.datos.pop(0)
            resultado = sum(self.datos)/len(self.datos)
            return resultado
        else:
            return None
    
f = Filtro(500)

ultimo= time.monotonic()
while True:
    valor = pot.value
    media = f.agregar(valor)
    if time.monotonic() - ultimo > 0.2:
        print(media)
        ultimo = time.monotonic()
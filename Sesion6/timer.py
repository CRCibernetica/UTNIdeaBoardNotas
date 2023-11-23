import time

class Timer:
    
    def __init__(self, tiempo):
        self.tiempo = tiempo
        self.ultimo = time.monotonic()
    
    def __str__(self):
        return f"Timer: {self.tiempo} seg"
        
    def listo(self):
        resultado = False
        if time.monotonic() - self.ultimo > self.tiempo:
            resultado = True
            self.ultimo = time.monotonic()
        return resultado
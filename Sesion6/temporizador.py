import time

class Temporizador:
    
    def __init__(self, tiempo):
        """
        Inicializa un temporizador con la duración especificada.

        Args:
            tiempo (float): La duración del temporizador en segundos.
        """
        self.tiempo = tiempo
        self.ultimo = time.monotonic()


    def __str__(self):
        """
        Devuelve una representación en cadena del temporizador.

        Returns:
            str: Una cadena formateada que indica la duración del temporizador.
        """
        return f"Temporizador: {self.tiempo} seg"
 
 
    def listo(self):
        """
        Verifica si el temporizador ha expirado.

        Returns:
            bool: True si el temporizador ha expirado, False en caso contrario.
        """
        resultado = False
        if time.monotonic() - self.ultimo > self.tiempo:
            resultado = True
            self.ultimo = time.monotonic()
        return resultado
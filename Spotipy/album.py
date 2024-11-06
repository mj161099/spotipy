from cancion import Cancion
from media import Media

class Album(Media):
    def __init__(self, titulo, artista, fecha_lanzamiento):
        super().__init__(titulo, artista)
        self.fecha_lanzamiento = fecha_lanzamiento
        self.canciones = []

    def add_cancion(self, cancion):
        self.canciones.append(cancion)

    def play(self):
        print(f"Reproduciendo album: {self.titulo} de {self.artista}")

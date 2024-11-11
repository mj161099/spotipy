from .album import Album
from .cancion import Cancion

class Artista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones_populares = []
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def add_cancion_popular(self, cancion, ruta):
        self.canciones_populares.append(cancion)

from .album import Album
from .cancion import Cancion

class Artista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones_populares = []
        self.albums = []

    def __str__(self):
        return self.nombre


    @classmethod
    def from_json(cls, data):
        artista = cls(data['nombre'])
        for album_data in data.get('albums', []):
            album = Album(
                album_data['titulo'],
                album_data['artista'],
                album_data['lanzamiento']
            )
            for cancion_data in album_data.get('canciones', []):
                cancion = Cancion(
                    cancion_data['titulo'],
                    cancion_data['artista'],
                    cancion_data['album'],
                    cancion_data['archivo'],
                    cancion_data['duracion']
                )
                album.add_cancion(cancion)
            artista.add_album(album)
        return artista

    def add_album(self, album):
        self.albums.append(album)

    def add_cancion_popular(self, cancion, ruta):
        self.canciones_populares.append(cancion)
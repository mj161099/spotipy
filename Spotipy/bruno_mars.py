from .album import Album
from .cancion import Cancion
from .artista import Artista

class BrunoMars(Artista):
    def __init__(self):
        super().__init__("Bruno Mars")

        album_24k_bruno_mars = Album("24K Magic", self.nombre, "2016")
        album_24k_bruno_mars.add_cancion(Cancion("That´s What I Like", self.nombre, "24K Magic", "C:That’s What I Like [Official Music Video] (1).wav", 190))
        album_24k_bruno_mars.add_cancion(Cancion("Versace on the Floor", self.nombre, "24K Magic", "Versace on the Floor (Single).wav", 250))
        self.albums.append(album_24k_bruno_mars)

        album_unorthodox_bruno_mars = Album("Unorthodox Jukebox", self.nombre, "2012")
        album_unorthodox_bruno_mars.add_cancion(Cancion("Locked out of Heaven", self.nombre, "Unorthodox Jukebox", "Bruno Mars - Locked Out Of Heaven (Official Music Video).wav", 210))
        album_unorthodox_bruno_mars.add_cancion(Cancion("When I Was Your Man", self.nombre, "Unorthodox Jukebox", "Bruno Mars - When I Was Your Man.wav", 200))
        self.albums.append(album_unorthodox_bruno_mars)       

    def __str__(self):
        return self.nombre
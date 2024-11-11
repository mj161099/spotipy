from .album import Album
from .cancion import Cancion
from .artista import Artista

class LuisFonsi (Artista):
	def __init__(self):
		super().__init__("Luis Fonsi")

		album_viaje_luis_fonsi = Album("El viaje", self.nombre, "Ultimo lanzamiento")
		album_viaje_luis_fonsi.add_cancion(Cancion("Roma", self.nombre, "El viaje", "Luis Fonsi, Laura Pausini - Roma (Official Video).wav", 200))
		album_viaje_luis_fonsi.add_cancion(Cancion("Andalucia", self.nombre, "El viaje", "Luis Fonsi - Andalucía (Visualizer).wav", 198))
		self.albums.append(album_viaje_luis_fonsi)

		album_8_luis_fonsi = Album("8", self.nombre, "2014")
		album_8_luis_fonsi.add_cancion(Cancion("Que Quieres De Mi", self.nombre, "8", "Que Quieres De Mi - Luis Fonsi 8 (Letra).wav", 260))
		album_8_luis_fonsi.add_cancion(Cancion("Llegaste Tú", self.nombre, "8", "Luis Fonsi - Llegaste Tú.wav", 211))
		self.albums.append(album_8_luis_fonsi)

	def __str__(self,):
		return self.nombre
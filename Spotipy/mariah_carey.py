from album import Album
from cancion import Cancion
from artista import Artista

class MariahCarey (Artista):
	def __init__(self):
		super().__init__("Mariah Carey")

		album_butterfly_mariah_carey = Album("Butterfly", self.nombre, "1997")
		album_butterfly_mariah_carey.add_cancion(Cancion("My All", self.nombre, "Butterfly", "My All.wav", 210))
		album_butterfly_mariah_carey.add_cancion(Cancion("Close My Eyes", self.nombre, "Butterfly", "Close My Eyes.wav", 252))
		self.albums.append(album_butterfly_mariah_carey)

		album_music_box_mariah_carey = Album("Music Box", self.nombre, "1993")
		album_music_box_mariah_carey.add_cancion(Cancion("Hero", self.nombre, "Music Box", "Mariah Carey - Hero.wav", 250))
		album_music_box_mariah_carey.add_cancion(Cancion("Without You", self.nombre, "Musi Box", "Mariah Carey - Without You.wav", 202))
		self.albums.append(album_music_box_mariah_carey)

	def __str__(self,):
		return self.nombre
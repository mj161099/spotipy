from media import Media

class Cancion(Media):
    def __init__(self, titulo, artista, album, ruta, duracion):
        super().__init__(titulo, artista)
        self.album = album
        self.ruta = ruta
        self.duracion = duracion

    def play(self):
        print(f"Reproduciendo cancion: {self.titulo} de {self.artista}")

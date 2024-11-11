from .artista import Artista

class Biblioteca:
    def __init__(self, usuario):
        self.usuario = usuario
        self.artistas_guardados = []

    def guardar_artista(self, artista):
        self.artistas_guardados.append(artista)

    def get_biblioteca_info(self):
        return {"Usuario": self.usuario.get_usuario_info(), "Artistas guardados": self.artistas_guardados}
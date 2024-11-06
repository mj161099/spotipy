from cancion import Cancion

class Playlist:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.canciones = []

    def añadir_cancion(self, cancion):
        self.canciones.append(cancion)

    @staticmethod
    def calcular_duracion_total(canciones):
        duracion_total = sum(cancion.duracion for cancion in canciones)
        return duracion_total

    @classmethod
    def contar_canciones(cls, canciones):
        return len(canciones)
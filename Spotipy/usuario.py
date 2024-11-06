from playlist import Playlist

class Usuario:
    def __init__(self, usuario_id, nombre, email, contraseña):
        self.usuario_id = usuario_id
        self.__nombre = nombre  # Atributo privado
        self.__email = email  # Atributo privado
        self.__contraseña = contraseña  # Atributo privado
        self.playlists = []

    # Getter para nombre
    @property
    def nombre(self):
        return self.__nombre

    # Setter para nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    # Getter para email
    @property
    def email(self):
        return self.__email

    # Setter para email
    @email.setter
    def email(self, email):
        self.__email = email

    # Getter para contraseña
    @property
    def contraseña(self):
        return self.__contraseña

    # Setter para contraseña
    @contraseña.setter
    def contraseña(self, contraseña):
        self.__contraseña = contraseña

    def crear_playlist(self, nombre):
        playlist = Playlist(nombre, self.usuario_id)
        self.playlists.append(playlist)
        return playlist

    def verificar_contraseña(self, contraseña):
        return self.__contraseña == contraseña

    def get_usuario_info(self):
        return {"usuario_id": self.usuario_id, "nombre": self.__nombre, "email": self.__email}
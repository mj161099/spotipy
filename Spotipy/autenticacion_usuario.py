from .usuario import Usuario

class AutenticacionUsuario:
    def __init__(self):
        self.usuarios = {}

    def registro_usuario(self, usuario_id, nombre, email, contraseña):
        if email in self.usuarios:
            return "\nEmail already registered."
        usuario = Usuario(usuario_id, nombre, email, contraseña)
        self.usuarios[email] = usuario
        return "\nUsuario registrado con exito."

    def login_usuario(self, email, contraseña):
        usuario = self.usuarios.get(email)
        if usuario and usuario.verificar_contraseña(contraseña):
            return f"\nBienvenido, {usuario.nombre}!"
        return "\nEmail o contraseña invalidos."
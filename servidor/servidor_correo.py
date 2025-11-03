from servidor.usuarios import usuarios

class ServidorCorreo:
    def __init__(self):
        self.usuarios = {}

    def agregar_usuario(self, usuario: usuarios):
        self.usuarios[usuario.email] = usuario
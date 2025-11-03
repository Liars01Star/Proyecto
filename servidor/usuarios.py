from servidor.carpeta import carpeta
from servidor.mensaje import mensaje

class usuarios:
    def __init__(self, nombre: str, contraseña: str, email: str):
        self.nombre = nombre
        self.__contraseña = contraseña
        self.email = email
        self.bandeja = carpeta("Bandeja de entrada")

    def existente(self, contraseña: str):
        return self.__contraseña == contraseña

    def recibir(self, msg: mensaje):
        self.bandeja.agregar_mensaje(msg)

    def listar(self):
        return self.bandeja

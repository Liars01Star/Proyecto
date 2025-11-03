from carpeta import carpeta
from mensaje import mensaje

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


if __name__ == "__main__":
    from usuarios import usuarios
    from mensaje import mensaje
    from usuarios import usuarios

    #Creación de correo como carpeta principal
    
    usuario = usuarios("Rodrigo", "contra123", "rodrigo@mail.com")

    m = mensaje("juan@mail.com", "rodrigo@mail.com", "Convención", "Este Viernes a las 15hs")
    usuario.recibir(m)

    print("Usuario:", usuario.nombre)
    print("Mensajes en el correo:", [msg.asunto for msg in usuario.bandeja.mensajes])
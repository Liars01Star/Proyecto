

class mensaje:
    def __init__(self, remitente: str, destinatario: str, asunto: str, cuerpo: str):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.cuerpo = cuerpo

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

class ServidorCorreo:
    def __init__(self):
        self.usuarios = {}
    def agregar_usuario(self, usuario: usuarios):
        self.usuarios[usuario.email] = usuario

class funciones_usuario:
    def __init__(self):
        self.usuarios = []

    def inicio_sesion(self):
        correo = input("Ingresa tu correo: ")
        contraseña = input("Ingresa tu contraseña: ")

        for u in self.usuarios:
            if u.email == correo and u.existente(contraseña):
                    print("\n¡bienvenido al sistema de correos!\n")
                    return u
        print("\nUsuario o contraseña incorrectos.\n")
        return None

    def creacion_usuario(self):
        nombre = input("nombre de usuario: ")
        contraseña = input("ingresa tu contraseña: ")
        email = input("ingresa tu correo: ")

        for u in self.usuarios:
            if u.nombre == nombre:
                print("\nusuario ya existente, proba con otro correo\n")
                return
        nuevo_usuario = usuarios(nombre, contraseña, email)
        self.usuarios.append(nuevo_usuario)
        print(f"\n{nombre} ingreso correctamente.\n")

    def listar_usuarios(self):
        if not self.usuarios:
            print("\nsin usuarios registrados.\n")
        else:
            print("\nusuarios registrados:")
            for u in self.usuarios:
                print(f"{u.nombre} ({u.email})")

    def enviar_mensaje(self, remitente, destinatario_email, asunto, cuerpo):
        destinatario = None
        for u in self.usuarios:
            if u.email == destinatario_email:
                destinatario = u
                break
        if destinatario:
            msg = mensaje(remitente.email, destinatario_email, asunto, cuerpo)
            destinatario.recibir(msg)
            print("\nMensaje enviado correctamente.")
        else:
            print("\ndestinatario inexistente.")

    def ver_bandeja(self, usuario):
        if not usuario.bandeja.mensajes:
            print("\nBandeja vacia.")
        else:
            print("\nTus mensajes:")
            for msg in usuario.bandeja.mensajes:
                print(f"Asunto: {msg.asunto}\nCuerpo: {msg.cuerpo}\n")

class carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []
        self.subcarpetas = []
    def agregar_subcarpeta(self, nombre): 
        nombre_normal = nombre.strip()
        if not nombre_normal:
            print("Nombre de subcarpeta vacio")
            return None
        for sub in self.subcarpetas:
            if sub.nombre.lower() == nombre_normal.lower():
                return sub
        nueva = carpeta(nombre_normal)
        self.subcarpetas.append(nueva)
        return nueva                               #Crea y agrega una subcarpeta (si no existe). Devuelve la subcarpeta."""
    def obtener_subcarpeta(self, nombre):
        nombre_normal =nombre.strip()
        for sub in self.subcarpetas:
            if sub.nombre.lower() == nombre_normal.lower():
                return sub
        return None                          #Devuelve la subcarpeta con ese nombre o None si no esta."""
    def eliminar_subcarpeta(self, nombre):
        nombre_normal = nombre.strip()
        for i, sub in enumerate(self.subcarpetas):
            if sub.nombre.lower() == nombre_normal.lower():
                self.subcarpetas.pop(i)
                return True
        return False              #"""Elimina la subcarpeta por nombre. Devuelve True/False segun el exito."""
    def agregar_mensaje(self, msg): 
        self.mensajes.append(msg)                #Agrega un mensaje a ESTA carpeta"""
    def eliminar_mensaje(self, msg):                #Saca un mensaje de ESTA carpeta. Devuelve True/False"""
        if msg in self.mensajes:
            self.mensajes.remove(msg)
            return True
        return False
    def mover_mensaje(self, msg, destino): #Mueve msg desde ESTA carpeta hacia "destino" (otra carpeta) """
        if self.eliminar_mensaje(msg):
            destino.agregar_mensaje(msg)
            return True
        return False
        pass
    def buscar(self, asunto=None, remitente=None): #esto es una busqueda recursiva
        resultados = []                                           #Busca en ESTA carpeta y en Todas sus subcarpetas (recursion).
        asun = asunto.lower() if asunto else None                #- si asunto es None, no filtra por asunto
        rem = remitente.lower() if remitente else None            #- si remitente es None, no filtra por remitente
        for msg in self.mensajes:                                 #Devuelve lista de mensajes que coinciden.
            coincide = True
            if asun is not None and asun not in msg.asunto.lower():         
                coincide = False
            if rem is not None and rem not in msg.remitente.lower():
                coincide = False
            if coincide:
                resultados.append(msg)
        for sub in self.subcarpetas:
            resultados.extend(sub.buscar(asunto, remitente))
        
        return resultados
    def listar(self, nivel=0):
        print ((" "* nivel) + self.nombre)
        for sub in self.subcarpetas:
            sub.listar(nivel + 1)# Muestra la estructura en arbol.#imprimi self.nombre con sangria (' ' * nivel) y llama#listar(nivel+1) en cada subcarpeta.
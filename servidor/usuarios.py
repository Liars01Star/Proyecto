from servidor.carpeta import carpeta
from servidor.mensaje import mensaje

class usuarios:
    def __init__(self, nombre: str, contraseña: str, email: str):
        self.nombre = nombre
        self.__contraseña = contraseña
        self.email = email
        self.reglas = []
        self.cola = []
        self.bandeja = carpeta("Bandeja de entrada")

    def encolar(self,msg):
        prio = msg.prioridad
        self.cola.append((prio, msg))
        self.cola.sort(key=lambda x: x[0], reverse=True) 

    def siguiente(self):
        if not self.cola:
            return None
        return self.cola.pop(0)[1]
    
    def ver_proximo(self):
        return self.cola[0][1] if self.cola else None
    
    def tamaño_cola(self):
        return len(self.cola)
    
    def vaciar_cola(self):
        self.cola.clear()
        
    def agregar_regla(self, condicion, accion, stop = True, nombre: str | None = None):
        self.reglas.append({
            "nombre": nombre,
            "condicion":condicion or {},
            "accion": accion or {},
            "stop": stop
            })
        
    def listar_reglas(self):
        return self.reglas
    
    def eliminar_regla(self, idx):
        if 0<=idx < len(self.reglas):
            self.reglas.pop(idx)
            return True
        return False
    
    def existente(self, contraseña: str):
        return self.__contraseña == contraseña

    def recibir(self, msg: mensaje):
        destino = self.bandeja
        
        def set_destino(carpeta_nueva):
            nonlocal destino
            destino = carpeta_nueva

        for regla in self.reglas:
            if self._matchea(msg, regla.get("condicion",{})):
                self._ejecutar_accion(msg, regla.get("accion", {}), out_destino = set_destino)
                if regla.get("stop",True):
                    break
        self.bandeja.agregar_mensaje(msg)
        
    def _matchea(self, msg: mensaje, condicion):
        if not condicion:
            return True
        
        asunto = msg.asunto.lower()
        remitente = msg.remitente.lower()
        etiquetas = (e.lower() for e in msg.etiquetas)

        if "asunto_contiene" in condicion:
            if condicion("asunto_contiene").lower() not in asunto:
                return False
        if "remitente_contiene" in condicion:
            if condicion("remitente_contiene").lower() not in remitente:
                return False
        if "tiene_etiqueta" in condicion:
            if condicion("tiene_etiqueta").lower() not in etiquetas:
                return False
            
        return True

    def ejecutar_accion(self, msg : mensaje, accion, out_destino):
        if not accion:
            return
        
        if "mover" in accion:
            sub = self.obtener_o_crear_subcarpeta(self.bandeja, accion("mover"))
            out_destino(sub)

        if "agregar_etiquetas" in accion:
            add_tag = accion("agregar_etiqueta")
            if isinstance(add_tag, list):
                for t in add_tag:
                    msg.agregar_etiqueta(t)
            else:
                msg.agregar_etiqueta(add_tag)
            
        if "quitar_etiqueta" in accion:
            rm_tag = accion("quitar_etiqueta")
            if isinstance(rm_tag, list):
                for t in rm_tag:
                    msg.quitar_etiqueta(t)
            else:
                msg.quitar_etiqueta(rm_tag)

        if "marcar_leido" in accion:
            if accion ("marcar leido"):
                msg.marcar_leido()
            else:
                msg.marcar_no_leido()

    def obtener_o_crear_subcarpeta(self, raiz: carpeta, nombre) -> carpeta:
        sub = raiz.obtener_subcarpeta(nombre)
        if not sub:
            sub = raiz.agregar_subcarpeta(nombre)
        return sub
    
    def listar(self):
        return self.bandeja
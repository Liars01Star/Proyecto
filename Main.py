from Servidor import ServidorCorreo, funciones_usuario

class menu:
    def __init__(self, fu, servidor):
        self.fu = fu
        self.servidor = servidor
        self.usuario_actual = None

    def menu_principal(self):
        while True:
            print("¿Que desea hacer?")
            print("1) Iniciar sesion")
            print("2) Crear usuario")
            print("3) Listar usuarios")
            print("4) Enviar mensaje")
            print("5) Ver bandeja")
            print("6) Crear subcarpeta")
            print("7) Mover mensaje a subcarpeta")
            print("8) Buscar bandeja")
            print("9) Ver mensajes de la carpeta")
            print("10) Cerrar sesión")
            print("0) Salir\n")

            #condicion para elegir la opción del menu
            opcion = input("opcion: ")
            if opcion == "1": 
                if not self.fu.usuarios:
                    print("\nSin usuarios registrados, crea uno antes de continuar")
                    continue
                usuario = self.fu.inicio_sesion()
                if usuario:
                    self.usuario_actual = usuario
            elif opcion == "2":
                self.fu.creacion_usuario()
            elif opcion == "3":
                self.fu.listar_usuarios()
            elif opcion == "4":
                if self.usuario_actual:
                    destinatario = input ("correo del destinatario: ")
                    asunto = input("asunto: ")
                    cuerpo = input("cuerpo del mensaje: ")
                    self.fu.enviar_mensaje(self.usuario_actual, destinatario, asunto, cuerpo)
                else:
                    print("\nAun no has iniciado sesión")
            elif opcion == "5":
                if self.usuario_actual:
                    self.fu.ver_bandeja(self.usuario_actual)
                else:
                    print("\nAun no has iniciado sesión")
            elif opcion == "6":
                if not self.usuario_actual:
                    print("\nPrimero incia sesion.")
                else:
                    nombre = input("Nombre de la nueva subcarpeta: ").strip()
                    if not nombre:
                        print("Nombre vacio")
                    else:
                        sub = self.usuario_actual.bandeja.agregar_subcarpeta(nombre)
                        if sub:
                            print(f"Subcarpeta '{sub.nombre}' creada.")
            elif opcion == "7":
                if not self.usuario_actual:
                    print("\nPrimero inicia sesion")
                else:
                    mensajes = self.usuario_actual.bandeja.mensajes
                    if not mensajes:
                        print("No hay mensajes en la carpeta.")
                    else:
                        print("\n Mensajes en carpeta: ")
                        for i, m in enumerate(mensajes, start=1):
                            print(f"{i}) {m.asunto} (De: {m.remitente}")
                        try:
                            idx = int(input("Elegi el numero de mensajes a mover: "))
                            if idx < 1 or idx > len(mensajes):
                                print("Indice invalido")
                            else:
                                msg = mensajes[idx - 1]
                                destino_nombre = input("Nombre de la subcarpeta destino: ").strip()
                                destino = self.usuario_actual.bandeja.obtener_subcarpeta(destino_nombre)
                                if not destino:
                                    print("La subcarpeta no existe.")
                                else:
                                    if self.usuario_actual.bandeja.mover_mensaje(msg, destino):
                                        print(f"Mensaje movido a '{destino.nombre}'.")
                                    else:
                                        print("No se pudo mover el mensaje.")
                        except ValueError:
                            print("Debes ingresar un numero.")
            elif opcion == "8":
                if not self.usuario_actual:
                    print("\nPrimero inicia sesion.")
                else:
                    asunto = input("Filtrar por asunto: ").strip()
                    remit = input("Filtrar por remitente: ").strip()
                    if asunto == "": asunto = None
                    if remit == "": remit = None
                    resultados = self.usuario_actual.bandeja.buscar(asunto=asunto, remitente=remit)
                    if not resultados:
                        print("\nSin coincidencias.")
                    else:
                        print(f"\nResultados ({len(resultados)}):")
                        for m in resultados:
                             print(f"- {m.asunto}  (De: {m.remitente})")
            elif opcion == "9":
                if not self.usuario_actual:
                    print("\nPrimero iniciá sesión.")
                else:
                    mensajes = self.usuario_actual.bandeja.mensajes
                    if not mensajes:
                        print("\nBandeja (raíz) vacía.")
                    else:
                        print("\nMensajes en la carpeta raíz:")
                    for m in mensajes:
                        print(f"Asunto: {m.asunto}\nCuerpo: {m.cuerpo}\n")
            elif opcion == "10":
                if self.usuario_actual:
                    print(f"\nSesión de {self.usuario_actual.nombre} finalizada.")
                    self.usuario_actual = None
                else:
                    print("\nNo hay sesión activa")
            elif opcion == "0":
                break
            else:
                print("\nOpción invalida")
if __name__ == "__main__":
    fu = funciones_usuario()
    servidor = ServidorCorreo()
    men= menu(fu, servidor)
    men.menu_principal()
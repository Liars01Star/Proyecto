from servidor.servidor_correo import ServidorCorreo
from funciones import funciones_usuario

class menu:
    def __init__(self, fu, servidor):
        self.fu = fu
        self.servidor = servidor
        self.usuario_actual = None

    def menu_sesion(self):
        while not self.usuario_actual:
            print("Bienvenido al sistema de correo, ¿que desea hacer?")
            print("1) Iniciar sesión")
            print("2) Crear usuario")
            print("3) Lista de usuario")
            print("0) Salir")

            opcion =input("Opción: ")

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

            elif opcion == "0":
                exit()

            else:
                print("\nOpción inválida")



    def menu_principal(self):
        while True:
            if not self.usuario_actual:
                self.menu_sesion()

            print("4) Enviar mensaje")
            print("5) Ver bandeja")
            print("6) Crear subcarpeta")
            print("7) Mover mensaje a subcarpeta")
            print("8) Buscar bandeja")
            print("9) Ver mensajes de la carpeta")
            print("10) Cerrar sesión")
            print("0) Salir\n")

            opcion = input("opcion: ")

            if opcion == "4":
                    self.fu.enviar_desde_usuario(self.usuario_actual)

            elif opcion == "5":
                    self.fu.ver_bandeja_completa(self.usuario_actual)

            elif opcion == "6":
                    self.fu.crear_subcarpeta(self.usuario_actual)

            elif opcion == "7":
                    self.fu.mover_mensaje(self.usuario_actual)

            elif opcion == "8":
                    self.fu.buscar_mensajes(self.usuario_actual)

            elif opcion == "9":
                    self.fu.ver_raiz(self.usuario_actual)

            elif opcion == "10":
                    print(f"\nSesión de {self.usuario_actual.nombre} finalizada.")
                    self.usuario_actual = self.fu.cerrar_sesion(self.usuario_actual)

            elif opcion == "0":
                 break

if __name__ == "__main__":
    fu = funciones_usuario()
    servidor = ServidorCorreo()
    men = menu(fu, servidor)
    men.menu_principal()
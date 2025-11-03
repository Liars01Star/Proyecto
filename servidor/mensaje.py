class mensaje:
    def __init__(self, remitente: str, destinatario: str, asunto: str, cuerpo: str):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.cuerpo = cuerpo

if __name__ == "__main__":
    from mensaje import mensaje

    mensaje = mensaje(
        asunto="Urgente",
        cuerpo="reunion de ejecutivos a las 11",
        remitente="ejecutivoficticio@mail.com",
        destinatario="ejecutivo2@mail.com"
    )

    print("Asunto:", mensaje.asunto)
    print("Cuerpo:", mensaje.cuerpo)
    print("Remitente:", mensaje.remitente)

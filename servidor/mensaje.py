class mensaje:
    def __init__(self, remitente: str, destinatario: str, asunto: str, cuerpo: str):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.cuerpo = cuerpo
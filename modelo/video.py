class Video:
    def __init__(self, id=None, titulo='', url='', assistido=False, quadro_id=None):
        self.id = id
        self.titulo = titulo
        self.url = url
        self.assistido = assistido
        self.quadro_id = quadro_id

    def __str__(self):
        return (
            f"Video("
            f"id={self.id}, "
            f"titulo='{self.titulo}', "
            f"url='{self.url}', "
            f"assistido={self.assistido}, "
            f"quadro_id={self.quadro_id}"
            f")"
        )

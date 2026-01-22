class Canal:
    def __init__(self, id=None, nome='', url='', descricao=''):
        self.id = id
        self.nome = nome
        self.url = url
        self.descricao = descricao

    def __str__(self):
        return (
            f"Canal("
            f"id={self.id}, "
            f"nome='{self.nome}', "
            f"url='{self.url}', "
            f"descricao='{self.descricao}'"
            f")"
        )
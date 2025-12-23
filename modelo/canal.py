class Canal:
    def __init__(self, id=None, nome=''):
        self.id = id
        self.nome = nome
        
    def __str__(self):
        return (
            f"Canal("
            f"id={self.id}, "
            f"nome='{self.nome}'"
            f")"
        )
class Quadro:
    def __init__(self, id=None, nome='', canal_id=None):
        self.id = id
        self.nome = nome
        self.canal_id = canal_id
        
    def __str__(self):
        return (
            f"Quadro("
            f"id={self.id}, "
            f"nome='{self.nome}', "
            f"canal_id={self.canal_id}"
            f")"
        )
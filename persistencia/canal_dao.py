class CanalDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, nome):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO canal (nome) VALUES (?)", (nome,))
        self.conexao.commit()
        return cursor.lastrowid

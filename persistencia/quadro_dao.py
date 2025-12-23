class QuadroDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, nome, canal_id):
        cursor = self.conexao.cursor()
        cursor.execute(
            "INSERT INTO quadro (nome, canal_id) VALUES (?, ?)",
            (nome, canal_id)
        )
        self.conexao.commit()
        return cursor.lastrowid

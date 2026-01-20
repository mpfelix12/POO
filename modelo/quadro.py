from modelo.conexao import conectar

class Quadro:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO quadro (nome, descricao) VALUES (?, ?)",
            (self.nome, self.descricao)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM quadro")
        dados = cursor.fetchall()
        conn.close()

        return [{"id": d[0], "nome": d[1]} for d in dados]

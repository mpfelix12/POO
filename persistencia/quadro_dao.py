from modelo.quadros import Quadro

class QuadroDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def criar(self, quadro):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO quadro (nome, descricao) VALUES (?, ?)", (quadro.nome, quadro.descricao))
        self.conexao.commit()
        return cursor.lastrowid

    def listar(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT id, nome, descricao FROM quadro")
        resultados = cursor.fetchall()
        quadros = []
        for linha in resultados:
            quadro = Quadro(linha[0], linha[1], linha[2])
            quadros.append(quadro)
        return quadros

    def buscar_por_id(self, id):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT id, nome, descricao FROM quadro WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Quadro(linha[0], linha[1], linha[2])
        return None

    def atualizar(self, quadro):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE quadro SET nome = ?, descricao = ? WHERE id = ?", (quadro.nome, quadro.descricao, quadro.id))
        self.conexao.commit()

    def deletar(self, quadro_id):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM quadro WHERE id = ?", (quadro_id,))
        self.conexao.commit()
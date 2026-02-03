from modelo.quadros import Quadro
from persistencia.conexao import conectar



class QuadroDAO:

    def criar(self, quadro):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO quadro (nome, descricao) VALUES (?, ?)", (quadro.nome, quadro.descricao))
        conn.commit()
        conn.close()
        return cursor.lastrowid

    def listar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, descricao FROM quadro")
        resultados = cursor.fetchall()
        conn.close()
        quadros = []
        for linha in resultados:
            quadro = Quadro(linha[0], linha[1], linha[2])
            quadros.append(quadro)
        return quadros

    def buscar_por_id(self, id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, descricao FROM quadro WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Quadro(linha[0], linha[1], linha[2])
        return None

    def atualizar(self, quadro):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE quadro SET nome = ?, descricao = ? WHERE id = ?", (quadro.nome, quadro.descricao, quadro.id))
        conn.commit()
        conn.close()

    def deletar(self, quadro_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM quadro WHERE id = ?", (quadro_id,))
        conn.commit()
        conn.close()
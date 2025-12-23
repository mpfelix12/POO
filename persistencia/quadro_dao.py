from modelo.quadro import Quadro

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
    
    def buscar_por_id(self, id):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM quadro WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Quadro(linha[0], linha[1], linha[2])
        return None
    
    def atualizar(self, quadro: Quadro):
        cursor = self.conexao.cursor()
        cursor.execute(
            "UPDATE quadro SET nome = ?, canal_id = ? WHERE id = ?",
            (quadro.nome, quadro.canal_id, quadro.id)
        )
        self.conexao.commit()
        
    def deletar(self, quadro_id):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM quadro WHERE id = ?", (quadro_id,))
        self.conexao.commit() 

from modelo.canal import Canal

class CanalDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, nome):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO canal (nome) VALUES (?)", (nome,))
        self.conexao.commit()
        return cursor.lastrowid
    
    def buscar_por_id(self, id):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM canal WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Canal(linha[0], linha[1])
        return None
    
    def atualizar(self, canal: Canal):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE canal SET nome = ? WHERE id = ?", (canal.nome, canal.id))
        self.conexao.commit()
        
    def deletar(self, canal_id):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM canal WHERE id = ?", (canal_id,))
        self.conexao.commit()

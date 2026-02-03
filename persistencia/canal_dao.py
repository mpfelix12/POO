from modelo.canal import Canal
from persistencia.conexao import conectar

class CanalDAO:

    def salvar(self, nome, url, descricao):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO canal (nome, url, descricao) VALUES (?, ?, ?)", (nome, url, descricao))
        conn.commit()
        conn.close()
        return cursor.lastrowid

    def buscar_por_id(self, id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM canal WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Canal(linha[0], linha[1], linha[2], linha[3])
        return None

    def atualizar(self, canal: Canal):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE canal SET nome = ?, url = ?, descricao = ? WHERE id = ?", (canal.nome, canal.url, canal.descricao, canal.id))
        conn.commit()
        conn.close()    

    def deletar(self, canal_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM canal WHERE id = ?", (canal_id,))
        conn.commit()
        conn.close()

    def listar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, url, descricao FROM canal")
        resultados = cursor.fetchall()
        canais = []
        for linha in resultados:
            canal = Canal(linha[0], linha[1], linha[2], linha[3])
            canais.append(canal)
        return canais
from modelo.usuario import Usuario

class UsuarioDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, usuario: Usuario):
        cursor = self.conexao.cursor()
        cursor.execute("""
            INSERT INTO usuario (nome, email, senha)
            VALUES (?, ?, ?)
        """, (usuario.nome, usuario.email, usuario.senha))
        self.conexao.commit()
        return cursor.lastrowid

    def buscar_por_id(self, id):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM usuario WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Usuario(linha[0], linha[1], linha[2], linha[3])
        return None

    def atualizar(self, usuario: Usuario):
        cursor = self.conexao.cursor()
        cursor.execute("""
            UPDATE usuario
            SET nome = ?, email = ?, senha = ?
            WHERE id = ?
        """, (usuario.nome, usuario.email, usuario.senha, usuario.id))
        self.conexao.commit()

    def deletar(self, usuario_id):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM usuario WHERE id = ?", (usuario_id,))
        self.conexao.commit()
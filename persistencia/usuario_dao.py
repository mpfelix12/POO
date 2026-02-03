from modelo.usuario import Usuario
from persistencia.conexao import conectar

class UsuarioDAO:
    
    def buscar_por_email_e_senha(self, email, senha):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM usuario WHERE email = ? AND senha = ?",
            (email, senha)
        )
        usuario = cursor.fetchone()
        conn.close()
        return usuario
    
    def salvar(self, usuario: Usuario):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO usuario (nome, email, senha)
            VALUES (?, ?, ?)
        """, (usuario.nome, usuario.email, usuario.senha))
        conn.commit()
        conn.close()
        return cursor.lastrowid

    def buscar_por_id(self, id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Usuario(linha[0], linha[1], linha[2], linha[3])
        return None

    def atualizar(self, usuario: Usuario):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE usuario
            SET nome = ?, email = ?, senha = ?
            WHERE id = ?
        """, (usuario.nome, usuario.email, usuario.senha, usuario.id))
        conn.commit()
        conn.close()

    def deletar(self, usuario_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuario WHERE id = ?", (usuario_id,))
        conn.commit()
        conn.close()
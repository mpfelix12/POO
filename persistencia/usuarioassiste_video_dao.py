from persistencia.conexao import conectar

class UsuarioAssisteVideoDAO:

    def marcar(self, id_usuario, id_video):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuario_assiste_video (id_usuario, id_video)
            VALUES (?, ?)
        """, (id_usuario, id_video))

        conn.commit()
        conn.close()

    def ja_assistiu(self, id_usuario, id_video):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 1 FROM usuario_assiste_video
            WHERE id_usuario = ? AND id_video = ?
        """, (id_usuario, id_video))

        resultado = cursor.fetchone()
        conn.close()
        return resultado is not None

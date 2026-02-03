import sqlite3

class UsuarioAssisteVideoDAO:
    def __init__(self):
        self.conn = sqlite3.connect("banco.db", check_same_thread=False)
        self.cursor = self.conn.cursor()

    def marcar_assistido(self, id_usuario, id_video):
        self.cursor.execute("""
            INSERT OR IGNORE INTO usuario_assiste_video (id_usuario, id_video)
            VALUES (?, ?)
        """, (id_usuario, id_video))
        self.conn.commit()

    def desmarcar_assistido(self, id_usuario, id_video):
        self.cursor.execute("""
            DELETE FROM usuario_assiste_video
            WHERE id_usuario = ? AND id_video = ?
        """, (id_usuario, id_video))
        self.conn.commit()

    def verificar_assistido(self, id_usuario, id_video):
        self.cursor.execute("""
            SELECT 1 FROM usuario_assiste_video
            WHERE id_usuario = ? AND id_video = ?
        """, (id_usuario, id_video))
        return self.cursor.fetchone() is not None

    def listar_assistidos_por_usuario(self, id_usuario):
        self.cursor.execute("""
            SELECT id_video FROM usuario_assiste_video
            WHERE id_usuario = ?
        """, (id_usuario,))
        return [linha[0] for linha in self.cursor.fetchall()]

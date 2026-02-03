from persistencia.conexao import conectar

class VideoDAO:

    def inserir(self, titulo, url, quadro_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO video (titulo, url, quadro_id) VALUES (?, ?, ?)",
            (titulo, url, quadro_id)
        )
        conn.commit()
        conn.close()

    def listar_por_quadro(self, quadro_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM video WHERE quadro_id = ?",
            (quadro_id,)
        )
        dados = cursor.fetchall()
        conn.close()
        return dados

    def marcar_concluido(self, video_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE video SET assistido = 1 WHERE id = ?",
            (video_id,)
        )
        conn.commit()
        conn.close()

    def existe_url_no_quadro(self, url, quadro_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 1 FROM video WHERE url = ? AND quadro_id = ?
        """, (url, quadro_id))

        existe = cursor.fetchone() is not None
        conn.close()
        return existe

    def excluir(self, id_video):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM video WHERE id = ?", (id_video,))
        conn.commit()
        conn.close()

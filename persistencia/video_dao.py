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

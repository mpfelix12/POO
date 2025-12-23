from modelo.video import Video

class VideoDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, video: Video):
        cursor = self.conexao.cursor()
        cursor.execute("""
            INSERT INTO video (titulo, url, assistido, quadro_id)
            VALUES (?, ?, ?, ?)
        """, (video.titulo, video.url, int(video.assistido), video.quadro_id))
        self.conexao.commit()
        return cursor.lastrowid

    def buscar_por_id(self, id):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM video WHERE id = ?", (id,))
        linha = cursor.fetchone()
        if linha:
            return Video(linha[0], linha[1], linha[2], bool(linha[3]), linha[4])
        return None
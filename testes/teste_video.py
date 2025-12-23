from persistencia.database import Database
from persistencia.canal_dao import CanalDAO
from persistencia.quadro_dao import QuadroDAO
from persistencia.video_dao import VideoDAO
from modelo.video import Video

db = Database()
conexao = db.conexao

canal_dao = CanalDAO(conexao)
quadro_dao = QuadroDAO(conexao)
video_dao = VideoDAO(conexao)

# 1️⃣ Criar Canal
canal_id = canal_dao.salvar("Canal POO")

# 2️⃣ Criar Quadro
quadro_id = quadro_dao.salvar("Quadro Aulas", canal_id)

# 3️⃣ Criar Vídeo
video = Video(
    titulo="Introdução à POO",
    url="https://youtube.com/abc",
    assistido=False,
    quadro_id=quadro_id
)

video_id = video_dao.salvar(video)

# 4️⃣ Buscar Vídeo
video_banco = video_dao.buscar_por_id(video_id)

print("Vídeo salvo e recuperado:")
print(video_banco.titulo)
print(video_banco.url)

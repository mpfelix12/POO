from persistencia.database import Database
from persistencia.canal_dao import CanalDAO
from persistencia.quadro_dao import QuadroDAO
from persistencia.video_dao import VideoDAO
from modelo.video import Video


def main():
    db = Database()
    conexao = db.conexao

    canal_dao = CanalDAO(conexao)
    quadro_dao = QuadroDAO(conexao)
    video_dao = VideoDAO(conexao)

    # Criar canal
    canal_id = canal_dao.salvar("Canal POO")

    # Criar quadro
    quadro_id = quadro_dao.salvar("Quadro Python", canal_id)

    # Criar vídeo
    video = Video(
        titulo="Introdução à POO",
        url="https://youtube.com/abc",
        assistido=False,
        quadro_id=quadro_id
    )

    video_id = video_dao.salvar(video)

    # Buscar vídeo
    video_banco = video_dao.buscar_por_id(video_id)

    print("Vídeo salvo e recuperado com sucesso:")
    print(video_banco)


if __name__ == "__main__":
    main()

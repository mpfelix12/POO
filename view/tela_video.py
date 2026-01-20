from modelo.video import Video
from modelo.quadro import Quadro
from telasUI.videoUI import VideoUI

class TelaVideo:
    def __init__(self):
        self.ui = VideoUI()

    def tela_videos(self):
        quadros = Quadro.listar()

        titulo, link, quadro_id = self.ui.formulario_cadastro(quadros)

        if titulo and link and quadro_id:
            Video(titulo, link, quadro_id).salvar()
            self.ui.mostrar_mensagem("Vídeo cadastrado com sucesso!")

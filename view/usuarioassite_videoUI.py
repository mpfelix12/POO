from persistencia.usuarioassiste_video_dao import UsuarioAssisteVideoDAO

class UsuarioAssisteVideoView:
    def __init__(self):
        self.dao = UsuarioAssisteVideoDAO()

    def marcar(self, id_usuario, id_video):
        self.dao.marcar_assistido(id_usuario, id_video)

    def desmarcar(self, id_usuario, id_video):
        self.dao.desmarcar_assistido(id_usuario, id_video)

    def ja_assistido(self, id_usuario, id_video):
        return self.dao.verificar_assistido(id_usuario, id_video)

    def listar_assistidos(self, id_usuario):
        return self.dao.listar_assistidos_por_usuario(id_usuario)

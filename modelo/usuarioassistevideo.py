from datetime import datetime

class UsuarioAssisteVideo:
    def __init__(self, id_usuario, id_video, data_marcado=None):
        self.__id_usuario = id_usuario
        self.__id_video = id_video
        self.__data_marcado = data_marcado or datetime.now()

    def get_id_usuario(self):
        return self.__id_usuario

    def get_id_video(self):
        return self.__id_video

    def get_data_marcado(self):
        return self.__data_marcado

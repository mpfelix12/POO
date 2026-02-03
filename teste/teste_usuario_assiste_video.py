from persistencia.usuarioassiste_video_dao import UsuarioAssisteVideoDAO

dao = UsuarioAssisteVideoDAO()

dao.marcar_assistido(1, 1)
print("Marcado!")

print("Já assistido?", dao.verificar_assistido(1, 1))

dao.desmarcar_assistido(1, 1)
print("Desmarcado!")

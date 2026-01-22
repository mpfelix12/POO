from view.canalUI import CanalUI
from modelo.canal import Canal

class TelaCanal:
    def __init__(self):
        self.ui = CanalUI()

    def cadastrar_canal(self):
        nome = self.ui.get_nome()
        link = self.ui.get_link()

        if nome and link:
            Canal(nome, link).salvar()
            self.ui.mostrar_mensagem("Canal salvo no banco com sucesso!")
        else:
            self.ui.mostrar_mensagem("Erro: campos obrigatórios.")

from view.quadroUI import QuadroUI
from modelo.quadros import Quadro

class TelaQuadro:
    def __init__(self):
        self.ui = QuadroUI()

    def cadastrar_quadro(self):
        nome = self.ui.get_nome()
        link = self.ui.get_link()

        if nome and link:
            Quadro(nome, link).salvar()
            self.ui.mostrar_mensagem("Quadro salvo no banco com sucesso!")
        else:
            self.ui.mostrar_mensagem("Erro: campos obrigatórios.")

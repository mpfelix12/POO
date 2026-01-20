from telasUI.quadroUI import QuadroUI
from modelo.quadro import Quadro

class TelaQuadro:
    def __init__(self):
        self.ui = QuadroUI()

    def cadastrar_quadro(self):
        nome = self.ui.get_nome()
        descricao = self.ui.get_descricao()

        if nome:
            Quadro(nome, descricao).salvar()
            self.ui.mostrar_mensagem("Quadro salvo no banco com sucesso!")
        else:
            self.ui.mostrar_mensagem("Nome é obrigatório!")

import streamlit as st
from persistencia.canal_dao import canalDAO

dao = canalDAO()

class CanalUI:
    def mostrar(self):
        st.title("Canais")

        canais = dao.listar()

        for c in canais:
            st.write(c[1])
    def __init__(self):
        st.subheader(" Cadastro de Canal")

    def get_nome(self):
        return st.text_input("Nome do canal")

    def get_link(self):
        return st.text_input("Link do canal")

    def mostrar_mensagem(self, mensagem):
        if "Erro" in mensagem:
            st.error(mensagem)
        else:
            st.success(mensagem)

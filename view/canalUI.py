import streamlit as st

class CanalUI:
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

import streamlit as st
from view.videoUI import TelaVideo
from view.quadroUI import QuadroUI
from view.canalUI import CanalUI

def menu():
    st.sidebar.title("Menu")

    opcao = st.sidebar.selectbox(
        "Escolha uma opção",
        ["Vídeos", "Quadros", "Canais"]
    )

    if opcao == "Vídeos":
        tela = TelaVideo()
        tela.mostrar()

    if opcao == "Quadros":
        quadro_ui = QuadroUI()
        quadro_ui.mostrar()

    if opcao == "Canais":
        canal_ui = CanalUI()
        canal_ui.mostrar()
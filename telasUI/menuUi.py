import streamlit as st
from telasUI.loginUI import tela_login
from telasUI.quadroUI import tela_quadros
from telasUI.videoUI import tela_videos
from telasUI.canalUI import tela_canais

def menu():
    if "logado" not in st.session_state:
        st.session_state["logado"] = False

    if not st.session_state["logado"]:
        tela_login()
    else:
        opcao = st.sidebar.selectbox(
            "Menu",
            ["Quadros", "Vídeos", "Canais"]
        )

        if opcao == "Quadros":
            tela_quadros()
        elif opcao == "Vídeos":
            tela_videos()
        elif opcao == "Canais":
            tela_canais()

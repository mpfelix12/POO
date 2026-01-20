import streamlit as st
from telasUI.videoUI import tela_videos
from view.tela_video import TelaVideo

def menu():
    st.sidebar.title("Menu")

    opcao = st.sidebar.selectbox(
        "Escolha uma opção",
        ["Vídeos", "Quadros", "Canais"]
    )

    if opcao == "Vídeos":
        tela_videos(TelaVideo())

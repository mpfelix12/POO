import streamlit as st
from persistencia.conexao import conectar
from persistencia.canal_dao import CanalDAO
from persistencia.quadro_dao import QuadroDAO

st.set_page_config(
    page_title="YTTrack",
    layout="wide"
)

# ================== CONEXÃO E DAOs ==================
# Inicializa a arquitetura do sistema
conn = conectar()

canal_dao = CanalDAO()
quadro_dao = QuadroDAO()

# ================== TELA INICIAL ==================
st.markdown(
    """
    <div style="text-align:center; margin-top:150px">
        <h1>🎬 Seja bem-vindo ao <span style="color:#6366f1">YTTrack</span></h1>
        <p style="font-size:18px">
            Plataforma para organização e acompanhamento de estudos com vídeos do YouTube.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.success("Sistema conectado ao banco de dados com sucesso!")

# ================== FECHAR CONEXÃO ==================
conn.close()

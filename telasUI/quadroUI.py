import streamlit as st
from persistencia.quadro_dao import QuadroDAO
from modelo.quadros import Quadro

st.set_page_config(page_title="YTTrack - Quadros", layout="wide")

st.markdown("## 📺 YTTrack")
st.divider()

col1, col2 = st.columns([8, 2])
col1.subheader("Quadros")

with col2:
    novo = st.button("Novo Quadro +")

dao = QuadroDAO()

if novo:
    with st.form("novo_quadro"):
        nome = st.text_input("Nome do Quadro")
        descricao = st.text_area("Descrição")
        salvar = st.form_submit_button("Salvar")

        if salvar:
            dao.criar(Quadro(None, nome, descricao))
            st.success("Quadro criado com sucesso")

quadros = dao.listar()

cores = ["#ff6b6b", "#b6e26d", "#5fd3c6", "#ff3b3b"]
cols = st.columns(2)

for i, q in enumerate(quadros):
    with cols[i % 2]:
        st.markdown(f"""
        <div style="
            background:{cores[i % len(cores)]};
            padding:20px;
            border-radius:12px;
            color:white;
            height:120px;
            margin-bottom:20px;
        ">
            <strong>{q.nome}</strong><br>
            <small>{q.descricao}</small>
        </div>
        """, unsafe_allow_html=True)

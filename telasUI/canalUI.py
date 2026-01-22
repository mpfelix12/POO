import streamlit as st
from persistencia.canal_dao import CanalDAO
from modelo.canal import Canal

st.set_page_config(page_title="YTTrack - Canais", layout="wide")

# Cabeçalho
st.markdown("## 📺 YTTrack")
st.divider()

st.subheader("Canais do YouTube")

dao = CanalDAO()

# ---------- FORMULÁRIO PARA NOVO CANAL ----------
with st.form("novo_canal"):
    nome = st.text_input("Nome do canal")
    url = st.text_input("Link do canal no YouTube")
    descricao = st.text_area("Descrição do canal")

    salvar = st.form_submit_button("Salvar canal")

    if salvar:
        canal = Canal(None, nome, url, descricao)
        dao.criar(canal)
        st.success("Canal salvo com sucesso!")

st.divider()

# ---------- LISTAGEM DE CANAIS ----------
canais = dao.listar()

if not canais:
    st.info("Nenhum canal cadastrado ainda.")
else:
    for canal in canais:
        st.markdown(
            f"""
            <div style="
                background:#f7f7f7;
                padding:18px;
                border-radius:12px;
                margin-bottom:15px;
            ">
                <strong>{canal.nome}</strong><br>
                <a href="{canal.url}" target="_blank">{canal.url}</a><br>
                <small>{canal.descricao}</small>
            </div>
            """,
            unsafe_allow_html=True
        )

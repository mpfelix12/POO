import streamlit as st
from persistencia.usuario_dao import UsuarioDAO
import hashlib

dao = UsuarioDAO()

st.title("Login")

email = st.text_input("Email")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    usuario = dao.buscar_por_email_e_senha(email, senha_hash)

    if usuario:
        st.session_state["usuario"] = usuario
        st.success("Login realizado com sucesso")
    else:
        st.error("Email ou senha inválidos")

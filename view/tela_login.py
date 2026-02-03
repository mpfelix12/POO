import streamlit as st
from persistencia.conexao import conectar
import hashlib

def tela_login():
    st.title("Login")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM usuario WHERE email=? AND senha=?",
            (email, senha_hash)
        )
        usuario = cursor.fetchone()
        conn.close()

        if usuario:
            st.session_state["usuario"] = usuario
            st.success("Login realizado")
        else:
            st.error("Dados inválidos")

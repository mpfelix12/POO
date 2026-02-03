import streamlit as st
from persistencia.usuario_dao import UsuarioDAO
from persistencia.database import conectar

st.title(" Login – YTTrack")

conn = conectar()
dao = UsuarioDAO(conn)

email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    usuario = dao.login(email, senha)
    if usuario:
        st.session_state.usuario = {
            "id": usuario.id_usuario,
            "nome": usuario.nome,
            "tipo": usuario.tipo_usuario
        }
        st.success("Login realizado!")
        st.switch_page("pages/2_Canais.py")
    else:
        st.error("E-mail ou senha inválidos")

conn.close()

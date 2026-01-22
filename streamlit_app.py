import streamlit as st

st.set_page_config(page_title="YTTrack", layout="centered")

# Controle de sessão
if "logado" not in st.session_state:
    st.session_state.logado = False

# LOGIN
if not st.session_state.logado:
    st.markdown("""
    <div style="text-align:center">
        <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" width="60">
        <h2>YTTrack</h2>
        <p>Login</p>
    </div>
    """, unsafe_allow_html=True)

    email = st.text_input("E-mail")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar", use_container_width=True):
        if email and senha:
            st.session_state.logado = True
            st.switch_page("pages/1_Quadros.py")
        else:
            st.error("Informe e-mail e senha")

import streamlit as st

def tela_login():
    st.markdown("<h1 style='text-align:center;'>YTTrack</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Login</h3>", unsafe_allow_html=True)

    st.markdown("---")

    email = st.text_input("E-mail")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        st.session_state["logado"] = True

    st.markdown(
        "<p style='text-align:center;'>Não tem uma conta? <a href='#'>Crie uma conta</a></p>",
        unsafe_allow_html=True
    )

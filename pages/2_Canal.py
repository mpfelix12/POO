import streamlit as st
from persistencia.conexao import conectar

st.title("Canais")

conn = conectar()
cursor = conn.cursor()
cursor.execute("SELECT * FROM canal")
canais = cursor.fetchall()
conn.close()

for canal in canais:
    st.subheader(canal[1])
   

if st.session_state.get("usuario") and st.session_state["usuario"][4] == "admin":
    st.divider()
    nome = st.text_input("Nome do canal")
    desc = st.text_area("Descrição")

    if st.button("Cadastrar"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO canal (nome, descricao) VALUES (?, ?)",
            (nome, desc)
        )
        conn.commit()
        conn.close()
        st.success("Canal cadastrado")

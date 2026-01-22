import streamlit as st
from persistencia.quadro_dao import QuadroDAO
from persistencia.database import conectar
from modelo.quadros import Quadro

# Obter a conexão com o banco de dados
conn = conectar()

# Passar a conexão para o QuadroDAO
dao = QuadroDAO(conn)

class QuadroUI:
    def __init__(self):
        self.dao = dao  # Use o QuadroDAO instanciado com a conexão

    def exibir_lista_de_quadros(self):
        quadros = self.dao.listar()
        if not quadros:
            st.info("Nenhum quadro cadastrado ainda.")
        else:
            cols = st.columns(2)
            for i, q in enumerate(quadros):
                with cols[i % 2]:
                    st.markdown(f"""
                    <div style="
                        background:#f0f0f0;
                        padding:15px;
                        border-radius:10px;
                    ">
                        <strong>{q.nome}</strong><br>
                        <small>{q.descricao}</small>
                    </div>
                    """, unsafe_allow_html=True)

    def formulario_de_cadastro(self):
        with st.form("novo_quadro"):
            nome = st.text_input("Nome do Quadro")
            descricao = st.text_area("Descrição")
            salvar = st.form_submit_button("Salvar")

            if salvar:
                if nome:
                    quadro = Quadro(None, nome, descricao)
                    self.dao.criar(quadro)
                    st.success("Quadro criado com sucesso")
                else:
                    st.error("O nome do quadro é obrigatório.")


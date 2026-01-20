import streamlit as st

def tela_quadro(controller):
    st.title("YTTrack")
    st.subheader("Quadros")

    controller.tela_quadros()
    
class QuadroUI:
    def formulario_cadastro(self, quadros):
        st.subheader("Cadastrar novo quadro")

        titulo = st.text_input("Título do quadro")
        link = st.text_input("Link do YouTube")

        quadro = st.selectbox(
            "Quadro",
            quadros,
            format_func=lambda q: q["nome"]
        )

        if st.button("Salvar vídeo"):
            return titulo, link, quadro["id"]

        return None, None, None

    def mostrar_mensagem(self, msg):
        st.success(msg)

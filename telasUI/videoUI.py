import streamlit as st

def tela_videos(controller):
    st.title("YTTrack")
    st.subheader("Vídeos")

    controller.tela_videos()

class VideoUI:
    def formulario_cadastro(self, quadros):
        st.subheader("Cadastrar novo vídeo")

        titulo = st.text_input("Título do vídeo")
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

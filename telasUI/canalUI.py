import streamlit as st

def tela_canal(controller):
    st.title("YTTrack")
    st.subheader("Canais")

    controller.tela_canais()
    
class CanalUI:
    def formulario_cadastro(self, quadros):
        st.subheader("Cadastrar novo canal")

        titulo = st.text_input("Título do canal")
        link = st.text_input("Link do YouTube")

        quadro = st.selectbox(
            "Quadro",
            quadros,
            format_func=lambda q: q["nome"]
        )

        if st.button("Salvar canal"):
            return titulo, link, quadro["id"]

        return None, None, None

    def mostrar_mensagem(self, msg):
        st.success(msg)

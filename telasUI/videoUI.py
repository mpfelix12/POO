import streamlit as st

def tela_videos():
    st.title("YTTrack")
    st.subheader("Vídeos")

    st.selectbox("Quadros", ["Nome do Quadro"])

    st.markdown("### Nome do Quadro")
    st.markdown("---")

    for _ in range(3):
        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(
                """
                <div style="
                    background:#e5e7eb;
                    height:70px;
                    border-radius:8px;
                    padding:10px;
                ">
                    <strong>Nome do vídeo</strong><br>
                    <small>Descrição</small>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.checkbox("Marcar como assistido")

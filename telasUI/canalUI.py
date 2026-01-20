import streamlit as st

def tela_canais():
    st.title("YTTrack")
    st.subheader("Canais")

    st.button("➕ Novo Canal")

    st.markdown("---")

    canais = [
        "Canal 1",
        "Canal 2",
        "Canal 3"
    ]

    for canal in canais:
        st.markdown(
            f"""
            <div style="
                background:#f3f4f6;
                border-radius:10px;
                padding:15px;
                margin-bottom:10px;
            ">
                <strong>{canal}</strong><br>
                <small>Descrição do canal</small>
            </div>
            """,
            unsafe_allow_html=True
        )

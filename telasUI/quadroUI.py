import streamlit as st

def tela_quadros():
    st.title("YTTrack")
    st.subheader("Quadros")

    st.button("➕ Novo Quadro")

    st.markdown("---")

    cores = ["#f87171", "#fde047", "#5eead4", "#ef4444"]
    cols = st.columns(4)

    for i, col in enumerate(cols):
        with col:
            st.markdown(
                f"""
                <div style="
                    background-color:{cores[i]};
                    height:140px;
                    border-radius:10px;
                    padding:10px;
                    font-weight:bold;
                ">
                    Nome do Quadro
                </div>
                """,
                unsafe_allow_html=True
            )

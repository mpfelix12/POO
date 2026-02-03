import streamlit as st
from persistencia.conexao import conectar

st.title("Quadros")

# ==========================
# Selecionar Canal
# ==========================
conn = conectar()
cursor = conn.cursor()
cursor.execute("SELECT id, nome FROM canal")
canais = cursor.fetchall()
conn.close()

if not canais:
    st.warning("Nenhum canal cadastrado.")
    st.stop()

canal_dict = {c[1]: c[0] for c in canais}
canal_nome = st.selectbox("Selecione o canal", canal_dict.keys())
canal_id = canal_dict[canal_nome]

# ==========================
# Listar Quadros do Canal
# ==========================
conn = conectar()
cursor = conn.cursor()
cursor.execute(
    "SELECT id, nome FROM quadro WHERE canal_id = ?",
    (canal_id,)
)



quadros = cursor.fetchall()
conn.close()

st.subheader("Quadros do canal")

if quadros:
    for quadro in quadros:
        st.markdown(f"### {quadro[1]}")
else:
    st.info("Este canal ainda não possui quadros.")

# ==========================
# Cadastro de Quadro (Admin)
# ==========================
if st.session_state.get("usuario") and st.session_state["usuario"][4] == "admin":
    st.divider()

    if st.button("Adicionar novo quadro"):
        st.session_state["novo_quadro"] = True

    if st.session_state.get("novo_quadro"):
        st.subheader("Novo quadro")
        nome_quadro = st.text_input("Nome do quadro")

        if st.button("Salvar quadro"):
            if not nome_quadro:
                st.error("Informe o nome do quadro")
            else:
                conn = conectar()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO quadro (nome, canal_id) VALUES (?, ?)",
                    (nome_quadro, canal_id)
                )
                conn.commit()
                conn.close()
                st.success("Quadro cadastrado com sucesso!")
                st.session_state["novo_quadro"] = False
                st.rerun()

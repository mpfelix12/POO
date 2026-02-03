import streamlit as st
from persistencia.database import conectar
from persistencia.canal_dao import CanalDAO
from persistencia.quadro_dao import QuadroDAO
from modelo.canal import Canal

st.set_page_config(page_title="YTTrack", layout="wide")

# ================== ESTADO DE NAVEGAÇÃO ==================
if "pagina" not in st.session_state:
    st.session_state.pagina = "canais"

if "canal_selecionado" not in st.session_state:
    st.session_state.canal_selecionado = None

# ================== MENU LATERAL ==================
st.sidebar.title("Menu")

opcao = st.sidebar.radio(
    "Navegação",
    ["Canais", "Quadros"]
)

if opcao == "Canais":
    st.session_state.pagina = "canais"
elif opcao == "Quadros":
    st.session_state.pagina = "quadros"

# ================== CONEXÃO ==================
conn = conectar()
canal_dao = CanalDAO(conn)
quadro_dao = QuadroDAO(conn)

# ================== PÁGINA DE CANAIS ==================
if st.session_state.pagina == "canais":
    st.title("Canais do YouTube")

    with st.form("novo_canal"):
        nome = st.text_input("Nome do canal")
        url = st.text_input("Link do canal no YouTube")
        descricao = st.text_area("Descrição do canal")

        salvar = st.form_submit_button("Salvar canal")

        if salvar:
            canal_dao.salvar(nome, url, descricao)
            st.success("Canal salvo com sucesso!")
            st.rerun()

    st.divider()

    canais = canal_dao.listar()

    if not canais:
        st.info("Nenhum canal cadastrado.")
    else:
        for canal in canais:
            col1, col2 = st.columns([4, 1])

            with col1:
                st.markdown(
                    f"""
                    <div style="background:#f7f7f7;padding:16px;border-radius:10px">
                        <strong>{canal.nome}</strong><br>
                        <a href="{canal.url}" target="_blank">{canal.url}</a><br>
                        <small>{canal.descricao}</small>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:
                if st.button("➡ Ver quadros", key=f"canal_{canal.id_canal}"):
                    st.session_state.canal_selecionado = canal
                    st.session_state.pagina = "quadros"
                    st.rerun()

# ================== PÁGINA DE QUADROS ==================
elif st.session_state.pagina == "quadros":
    canal = st.session_state.canal_selecionado

    if not canal:
        st.warning("Selecione um canal primeiro.")
    else:
        st.title(f"Quadros do canal: {canal.nome}")

        with st.form("novo_quadro"):
            nome = st.text_input("Nome do quadro")
            descricao = st.text_area("Descrição do quadro")

            salvar = st.form_submit_button("Salvar quadro")

            if salvar:
                quadro_dao.salvar(canal.id_canal, nome, descricao)
                st.success("Quadro cadastrado!")
                st.rerun()

        st.divider()

        quadros = quadro_dao.listar_por_canal(canal.id_canal)

        if not quadros:
            st.info("Nenhum quadro cadastrado para este canal.")
        else:
            for quadro in quadros:
                st.markdown(
                    f"""
                    <div style="background:#eef2ff;padding:14px;border-radius:10px;margin-bottom:10px">
                        <strong>{quadro.nome}</strong><br>
                        <small>{quadro.descricao}</small>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# ================== FECHAR CONEXÃO ==================
conn.close()

import streamlit as st
from persistencia.quadro_dao import QuadroDAO
from persistencia.video_dao import VideoDAO
from persistencia.usuarioassiste_video_dao import UsuarioAssisteVideoDAO


quadro_dao = QuadroDAO()
video_dao = VideoDAO()
progresso_dao = UsuarioAssisteVideoDAO()


st.title("Vídeos")

# 🔐 Verifica se o usuário está logado
usuario = st.session_state.get("usuario")
if not usuario:
    st.warning("Faça login para acessar os vídeos")
    st.stop()

# 📌 Selecionar quadro
quadros = quadro_dao.listar()
quadro_ids = [q[0] for q in quadros]
quadro_nomes = {q[1]: q[0] for q in quadros}

quadro_nome = st.selectbox("Selecione o quadro", quadro_nomes.keys())
quadro_id = quadro_nomes[quadro_nome]

# ============================
# 👇 A PARTIR DAQUI ENTRA SEU CÓDIGO
# ============================

if usuario and usuario[4] == "admin":
    st.divider()

    if st.button(" Adicionar novo vídeo"):
        st.session_state["novo_video"] = True

    if st.session_state.get("novo_video"):
        st.subheader("Novo vídeo")

        titulo = st.text_input("Título do vídeo")
        url = st.text_input("URL do YouTube")

        if st.button("Salvar vídeo"):
            if not titulo or not url:
                st.error("Preencha todos os campos")
            elif video_dao.existe_url_no_quadro(url, quadro_id):
                st.error("Este vídeo já existe neste quadro")
            else:
                video_dao.inserir(titulo, url, quadro_id)
                st.success("Vídeo cadastrado com sucesso!")
                st.session_state["novo_video"] = False
                st.rerun()


videos = video_dao.listar_por_quadro(quadro_id)

for v in videos:
    id_video = v[0]
    titulo = v[2]
    url = v[3]

    st.subheader(titulo)
    st.video(url)

    id_usuario = usuario[0]

    if progresso_dao.ja_assistiu(id_usuario, id_video):
        st.success("✔ Vídeo concluído")
    else:
        if st.button("Marcar como concluído", key=id_video):
            progresso_dao.marcar(id_usuario, id_video)
            st.success("Vídeo marcado como assistido")


    if usuario and usuario[4] == "admin":
        if st.button("Excluir vídeo", key=f"del_{id_video}"):
            video_dao.excluir(id_video)
            st.warning("Vídeo excluído")
            st.rerun()

import streamlit as st
from persistencia.database import conectar
from persistencia.video_dao import VideoDAO
from persistencia.quadro_dao import QuadroDAO
from modelo.video import Video

st.set_page_config(page_title="YTTrack - Vídeos", layout="wide")

st.markdown("##  YTTrack")
st.divider()
st.subheader("Vídeos")

if "conexao" not in st.session_state:
    st.session_state.conexao = conectar()

quadro_dao = QuadroDAO(st.session_state.conexao)
quadros = quadro_dao.listar()

mapa = {q.nome: q.id for q in quadros}
quadro_nome = st.selectbox("Quadros", mapa.keys())
quadro_id = mapa[quadro_nome]

# FORMULÁRIO PARA RECEBER LINK DO YOUTUBE
with st.form("novo_video"):
    titulo = st.text_input("Nome do vídeo")
    url = st.text_input("Link do YouTube")
    salvar = st.form_submit_button("Salvar vídeo")

    if salvar:
        video = Video(None, titulo, url, False, quadro_id)
        VideoDAO().criar(video)
        st.success("Vídeo salvo com sucesso")

st.divider()

# LISTAGEM DE VÍDEOS
videos = VideoDAO().listar_por_quadro(quadro_id)

for v in videos:
    col1, col2 = st.columns([7, 3])

    col1.markdown(f"""
    <div style="
        background:#f0f0f0;
        padding:15px;
        border-radius:10px;
    ">
        <strong>{v.titulo}</strong><br>
        <a href="{v.url}" target="_blank">{v.url}</a>
    </div>
    """, unsafe_allow_html=True)

    assistido = col2.checkbox("Marcar como assistido", value=v.assistido, key=v.id)
    if assistido != v.assistido:
        VideoDAO().marcar_assistido(v.id, assistido)

import streamlit as st
from persistencia.video_dao import VideoDAO

dao = VideoDAO()

st.title("Vídeos")

quadro_id = st.selectbox("Quadro", quadros_ids)
videos = dao.listar_por_quadro(quadro_id)

for v in videos:
    st.subheader(v[1])
    st.video(v[2])
    
    if st.button(f"Marcar como assistido - {v[1]}"):
        dao.marcar_concluido(v[0])
        st.success("Vídeo concluído")
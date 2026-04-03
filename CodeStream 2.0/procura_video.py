import streamlit as st
import add_video, procura_video
from streamlit_player import st_player
from database import Video, dba

def procure():
    
        
    st.title("Bem-Vindo a Página Para procurar algum Vídeo desejado")
    nomes =st.text_input("Digite o Tema do Vídeo: ")
    if st.button("Procurar"):
        if not nomes:
            st.error("Por favor, preencha todos os campos.")
            return
        if nomes:
            
            video = Video.select().where(Video.Nome.contains(nomes))
            
            
        
        if video:
            for v in video:
                with st.expander(f"Assistir: {v.Nome}", expanded=True):                   
                    st_player(v.Url)
        else:
            st.error("Video Não Encotrado")
    
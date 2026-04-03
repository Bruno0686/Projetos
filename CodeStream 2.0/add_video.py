import streamlit as st
import streamlit_player
from database import Video, dba

dba.create_tables([Video], safe=True)

def add():
    st.title("Bem-Vindo a Página Para Adicionar algum Vídeo desejado")

    nome = st.text_input("Digite o Nome do Vídeo: ")
    url = st.text_input("URL do Vídeo (Apenas YouTube ou Link Direto: ")
    if st.button("Adicionar"):
        if url == url:(str)
        if nome and url:
                Video.create(Nome = nome, Url= url)
                st.success("Adicionado com Sucesso.")
    else:
        st.error("Preencha Todos os Campos!")


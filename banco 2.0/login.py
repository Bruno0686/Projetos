import streamlit as st
from database import Usuario


def app():
    img_url = "https://i.imgur.com/niU2URZ.jpeg" 
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                        url("{img_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True
    )
    st.info("Caso esteja no tema branco, clique nos tres pontinhos no canto superior direito e mude para o tema escuro para melhor visualização.")
    st.title("Login no GUBR-Bank")
    st.write("Bem-vindo à página de login do GUBR-Bank!")

    agencia_digitada = st.text_input(
        "Agência",
    )

    senha_digitada = st.text_input(
        "Senha",
        type="password"
    )

    if st.button("Logar"):
        if not agencia_digitada or not senha_digitada:
            st.error("Por favor, preencha todos os campos.")
            return

        usuario = Usuario.get_or_none(
            (Usuario.agencia == agencia_digitada) &
            (Usuario.senha == senha_digitada)
        )

        if usuario:
         
            st.session_state.logado = True
            st.session_state.agencia = usuario.agencia
            st.session_state.nome = usuario.nome
            st.session_state.usuario_id = usuario.id

            st.success("Bem-vindo ao GUBR-Bank!")
            st.rerun() 
        else:
            st.error("Agência ou senha inválidos.")

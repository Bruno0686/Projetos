import streamlit as st
from database import Conta


def app():
    st.title("Login no CodeStream")

    email_digitada = st.text_input(
        "Email",
    )

    senha_digitada = st.text_input(
        "Senha",
        type="password"
    )

    if st.button("Logar"):
        if not email_digitada or not senha_digitada:
            st.error("Por favor, preencha todos os campos.")
            return

        conta = Conta.get_or_none(
            (Conta.email == email_digitada) &
            (Conta.senha == senha_digitada)
        )

        if conta:
         
            st.session_state.logado = True
            st.session_state.agencia = conta.email
            st.session_state.nome = conta.nome
            st.session_state.usuario_id = conta.id

            st.success("Bem-vindo ao CodeStream!")
            st.rerun() 
        else:
            st.error("Email ou senha inválidos.")

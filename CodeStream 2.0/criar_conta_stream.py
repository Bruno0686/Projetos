import streamlit as st




from database import Conta
from database import dbs

dbs.create_tables([Conta], safe=True)

def app():
    st.title("Criação de Conta No CodeStream")


    nome = st.text_input(
        "Nome Completo",
        key="criar_nome"
    )
    email = st.text_input(
        "Email",
        key="criar_email"
    )
    senha = st.text_input(
        "Senha",
        type="password",
        key="criar_senha"
    )

    if st.button("Criar Conta", key="btn_criar_conta"):
        if not nome or not email or not senha:
            st.error("Por favor, preencha todos os campos.")
            return

        if Conta.select().where(Conta.email == email).exists():
            st.error("Email já cadastrado. Por favor, escolha outro.")
            return

        try:
            conta = Conta.create(
                nome=nome,
                email=email,
                senha=senha
            )

            st.success(f"Conta criada com sucesso para **{nome}**!")
        
            if conta:
                st.session_state.logado = True
                st.session_state.email = conta.email
                st.session_state.nome = conta.nome
                st.session_state.id = conta.id
                st.rerun()  
        except Exception as e:   

            st.error(f"Ocorreu um erro ao criar a conta: {e}")
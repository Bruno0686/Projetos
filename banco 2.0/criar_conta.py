import streamlit as st
from database import Usuario, db

db.create_tables([Usuario], safe=True)

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
    st.title("Criar Conta no GUBR-Bank")
    st.write("Bem-vindo à página de criação de conta do GUBR-Bank!")

    nome = st.text_input(
        "Nome Completo",
        key="criar_nome"
    )
    agencia = st.text_input(
        "Agência",
        key="criar_agencia"
    )
    senha = st.text_input(
        "Senha",
        type="password",
        key="criar_senha"
    )

    if st.button("Criar Conta", key="btn_criar_conta"):
        if not nome or not agencia or not senha:
            st.error("Por favor, preencha todos os campos.")
            return

        if Usuario.select().where(Usuario.agencia == agencia).exists():
            st.error("Agência já existe. Por favor, escolha outra.")
            return

        try:
            usuario = Usuario.create(
                nome=nome,
                agencia=agencia,
                senha=senha,
                saldo=0.00
            )

            st.success(f"Conta criada com sucesso para **{nome}**!")
        
            if usuario:
                st.session_state.logado = True
                st.session_state.agencia = usuario.agencia
                st.session_state.nome = usuario.nome
                st.session_state.usuario_id = usuario.id

                st.rerun()  
        except Exception as e:   

            st.error(f"Ocorreu um erro ao criar a conta: {e}")
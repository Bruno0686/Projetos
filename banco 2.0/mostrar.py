import streamlit as st
from database import Usuario

def ver():
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
    st.title("📄 Mostrar sua Conta")

    if "logado" not in st.session_state or not st.session_state.logado:
        st.warning("Faça login para acessar esta página.")
        st.rerun()
        return

    agencia = st.session_state.get("agencia")

    if not agencia:
        st.error("Agência não encontrada na sessão.")
        return

    usuario = Usuario.get_or_none(Usuario.agencia == agencia)

    if usuario:
        st.success("Conta encontrada!")

        with st.container(border=True):
            st.subheader(f"Dados da Conta: {usuario.nome}")
            st.info(f"💰 Saldo Atual: R$ {usuario.saldo:.2f}")
            st.text(f"Agência: {usuario.agencia}")
            
    else:
        st.error("Usuário não encontrado.")

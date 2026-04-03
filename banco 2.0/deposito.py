import streamlit as st
from database import Usuario


def dep():
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
    st.session_state["pagina"] = "deposito"

    st.title("💵 Depósito")

    if not st.session_state.get("logado") or not st.session_state.get("agencia"):
        st.warning("Faça login para acessar esta página.")
        return

    agencia = st.session_state.agencia
    usuario = Usuario.get_or_none(Usuario.agencia == agencia)

    if not usuario:
        st.error("Usuário não encontrado.")
        return

    st.write(f"**Saldo Atual:** R$ {usuario.saldo:.2f}")

    valor_deposito = st.number_input(
        "Valor do Depósito (R$)",
        min_value=0.01,
        step=10.0,
        format="%.2f",
        key="valor_deposito"
    )

    if st.button("Confirmar Depósito", key="btn_deposito"):
        usuario.saldo += valor_deposito
        usuario.save()

        st.success(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
        st.info(f"Novo saldo: R$ {usuario.saldo:.2f}")
    

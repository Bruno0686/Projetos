import streamlit as st
from database import Usuario


def saq():
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
    st.session_state["pagina"] = "saque"

    st.title("💵 Saque")

    if not st.session_state.get("logado") or not st.session_state.get("agencia"):
        st.warning("Faça login para acessar esta página.")
        return

    agencia = st.session_state.agencia
    usuario = Usuario.get_or_none(Usuario.agencia == agencia)

    if not usuario:
        st.error("Usuário não encontrado.")
        return

    st.write(f"**Saldo Atual:** R$ {usuario.saldo:.2f}")

    valor_saque = st.number_input(
        "Valor do saque (R$)",
        min_value=0.01,
        step=10.0,
        format="%.2f",
        key="valor_saque"
    )
    if usuario.saldo<valor_saque:
        st.error("Saldo insuficiente para este saque.")
        return
    if st.button("Confirmar Saque", key="bnt_saque"):
        usuario.saldo -= valor_saque
        usuario.save()

        st.success(f"O Saque de R$ {valor_saque:.2f} realizado com sucesso!")
        st.info(f"Novo saldo: R$ {usuario.saldo:.2f}")

import streamlit as st
from streamlit_option_menu import option_menu
import login
import criar_conta
import deposito  
import mostrar
import saque
import inicial

st.set_page_config(
    page_title="GUBR-Bank",
    layout="centered"
)

def banco():
    if "logado" not in st.session_state:
        st.session_state.logado = False

    if "page" not in st.session_state:
        st.session_state.page = "Login"

    if not st.session_state.logado:
        with st.sidebar:
            escolha = option_menu(
                menu_title="GUBR-Bank",
                options=["Login", "Criar Conta"],
                icons=["person-check", "person-add"],
                menu_icon="bank",
                default_index=0,
                styles={
                    "container": {"padding": "5px", "background-color": "#000000"},
                    "nav-link": {"color": "white", "font-size": "18px"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )
        
        if escolha == "Login":
            login.app()
        elif escolha == "Criar Conta":
            criar_conta.app()
        elif escolha == "Saque":
            saque.saq
            
    else:
        with st.sidebar:
            escolha_logado = option_menu(
                menu_title="Área do Cliente",
                options=["Inicio", "Depósito","Saque", "Mostrar", "Sair" ],
                icons=["house", "cash-stack", "cash-stack", "person-circle",  "door-open"],
                menu_icon="wallet2",
                default_index=0,
                styles={
                    "container": {"padding": "5px", "background-color": "#000000"},
                    "nav-link": {"color": "white", "font-size": "18px"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )

        if escolha_logado == "Inicio":
           inicial.home()
        elif escolha_logado == "Depósito":
            deposito.dep() 

        elif escolha_logado == "Mostrar":
            mostrar.ver()
        
        elif escolha_logado == "Saque":
            saque.saq()
            
        elif escolha_logado == "Sair":
            st.session_state.logado = False
            st.rerun()

if __name__ == "__main__":
    banco()
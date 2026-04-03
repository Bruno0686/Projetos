import streamlit as st
from streamlit_option_menu import option_menu
import login_stream, criar_conta_stream
import add_video, procura_video

def mainstream():
    seleção_logado = None
    if "logado" not in st.session_state:
        st.session_state.logado = False

    if "page" not in st.session_state:
        st.session_state.page = "Login"

    if not st.session_state.logado:
        with st.sidebar:
            escolha = option_menu(
                menu_title="CodeStream",
                options=["Login", "Criar Conta"],
                icons=["person-check", "person-add"],
                menu_icon="play",
                default_index=0,
                styles={
                    "container": {"padding": "5px", "background-color": "#000000"},
                    "nav-link": {"color": "white", "font-size": "18px"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )
        
        if escolha == "Login":
            login_stream.app()
        elif escolha == "Criar Conta":
            criar_conta_stream.app()

    else: 
        with st.sidebar:
            seleção_logado = option_menu(
                menu_title="Navegação de videos",
                options=["Adicionar", "procurar", "Sair"],
                icons=["plus", "search", "door-open"],
                menu_icon="play",
                default_index=0,
                styles={
                    "container": {"padding": "5px", "background-color": "#000000"},
                    "nav-link": {"color": "white", "font-size": "18px"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )
                        

    
    if seleção_logado == "Adicionar":
        add_video.add()
    elif seleção_logado == "procurar":
        procura_video.procure()
    elif seleção_logado == "Sair":
        st.session_state.logado = False
        st.rerun()

if __name__ == "__main__":
    mainstream()












    

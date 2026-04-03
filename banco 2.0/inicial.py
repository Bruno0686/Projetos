import streamlit as st


def home():
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
    st.title(f"Bem-vindo  ao GUBR-Bank!")
        

    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="{"https://i.imgur.com/zwtatQI.png"}" width="300">
        </div>
        """,
        unsafe_allow_html=True)
    st.write("Selecione uma operação no menu lateral.")

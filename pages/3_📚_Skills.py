import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Skills",
    page_icon="🏃🏼",
    layout="wide"
)

st.sidebar.markdown("Desenvolvido por Gilson Dias [Linkedin](https://www.linkedin.com/in/gilson-dias-jn/) [GitHub](https://github.com/G1lsJn)")


# Adicionando o logo
st.logo("logo_google.png")

# Adicionando a foto de perfil no body
st.image("perfil.png", width=150)

st.title("📌 Skills")


st.write("""
        * Pyhton
        * Java
        * C
        * HTML
        * JavaScript
        * CSS
        * MySql
        * UX/UI
        * Design Thinking
        * Domínio do Microsoft Office (Word, Excel, PowerPoint)
        * Excelentes habilidades organizacionais, multitarefas e resolução de problemas
        * Facilidade em trabalhar em equipe     
        * Inglês: intermediário (leitura, fala); básico (escrita)
         
        """)





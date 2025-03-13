import streamlit as st
import pandas as pd
from streamlit_extras.app_logo import add_logo

if "data" not in st.session_state:
    df = pd.read_excel("Dados.xlsx", index_col="ID_Empresa")
    df = df.sort_values(by="Número de empresas", ascending=False)
    df = df.astype({col: "int" for col in df.select_dtypes("number").columns})
    st.session_state["data"] = df

# Configuração da página
st.set_page_config(page_title="Dashboard Profissional - Gilson Dias", layout="wide")
st.sidebar.markdown("Desenvolvido por Gilson Dias [Linkedin](https://www.linkedin.com/in/gilson-dias-jn/) [GitHub](https://github.com/G1lsJn)")

# Adicionando o logo
st.logo("logo_google.png")

c1, c2 = st.columns([0.5,0.5])

# Adicionando a foto de perfil no body
c1.image("perfil.png", width=150)

c1.title("Gilson Dias Ramos Junior")

c1.write("Sou formado no curso técnico em Desenvolvimento de Sistemas na ETEC de Franco da Rocha e, desde então, mergulhei na área da tecnologia. Atualmente, estou cursando Engenharia de Software na FIAP e me preparando para entrar no mercado de trabalho. A faculdade me proporciona a chance de participar de projetos em grupo, simulando o ambiente empresarial e de fazer cursos que complementam minha formação. Mal posso esperar para trilhar minha jornada e fazer parte desse mundo da tecnologia, sempre aprendendo e crescendo!")


c1.write("")

c1.write("### Minhas redes ")
c1.markdown("[Linkedin](https://www.linkedin.com/in/gilson-dias-jn/)")
c1.markdown("[GitHub](https://github.com/G1lsJn)")

c1.write("")

c1.title("Objetivo Profissional")

c1.write("Desenvolvedor de software em busca de oportunidades para aplicar e expandir conhecimentos em desenvolvimento de sistemas e web. Interesse em novas tecnologias e em contribuir para projetos inovadores que agreguem valor ao negócio.")



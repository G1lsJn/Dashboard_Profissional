import streamlit as st

st.set_page_config(
    page_title="Formações e Experiencias",
    page_icon="🎓",
    layout="wide"
)

st.sidebar.markdown("Desenvolvido por Gilson Dias [Linkedin](https://www.linkedin.com/in/gilson-dias-jn/) [GitHub](https://github.com/G1lsJn)")


# Adicionando o logo
st.logo("logo_google.png")

# Adicionando a foto de perfil no body
st.image("perfil.png", width=150)

st.write("")
st.write("")

c1, c2 = st.columns([0.5,0.5])

# Formações
c1.title("Formação Acadêmica")

c1.write("")

c1.write("**FIAP – FACULDADE DE INFORMÁTICA E ADMINISTRAÇÃO PAULISTA**")
c1.write("*Bacharelado em Engenharia de Software (AGO/2023 - JUL/2027*)")
c1.image("logo_fiap.png", width=150)

c1.write("**E.T.E.C. Dr. Emílio Hernandez Aguilar**")
c1.write("*Técnico em Desenvolvimento de Sistemas (FEV/2020 - JUN/2021)*")
c1.image("logo_etec.png", width=150)

# Cursos complementares
c2.title("Cursos complementares")

c2.write("")


c2.write("""
* Formação Social e Sustentabilidade – FIAP (05/2023).
* JavaScript e HTML: Desenvolva um jogo e pratique lógica de programação – Alura (06/2023).
* Biohacking, Deep web e Criptografia – FIAP (09/2023).
* Design Thinking Process – FIAP (10/2023)
* Chatgpt: desvendando a IA em conversas e suas aplicações - Alura (10/2023)
* Java: Criando a sua primeira aplicação - Alura (10/2023)
* Python: começando com a linguagem – Alura (10/2024)
* Python: crie a sua primeira aplicação - Alura (02/2024)
* Lógica de programação: mergulhe em programação com JavaScript – Alura (02/2024)
* Lógica de programação: Explore funções e listas – Alura (02/2024)
* Python: aplicando a orientação a objetos – Alura (02/2024)
* HTML e CSS: Ambientes de desenvolvimento, estrutura de arquivos e tags – Alura (02/2024)
""")

col1, col2, col3 = c2.columns([0.25,0.25, 0.5])

col1.image("logo_alura.png", width=140)
col2.image("logo_nano.png", width=150)


# Experiencias
st.title("Experiências")

st.write("")

st.write("### Projeto para o ICr")

st.write("""
Participação em projeto para o Instituto da Criança e do Adolescente (ICr) do Hospital das Clínicas. Nesse projeto desenvolvi as seguintes habilidades:
* Co-desenvolvimento de uma plataforma interativa infantil utilizando Python, HTML, CSS e JavaScript.
* Aplicação de práticas de UX/UI para garantir a usabilidade do sistema para crianças.
* Projeto final apresentado com excelência, destacando-se pela inovação e pela gestão eficaz em equipe.
""")

st.markdown("Link do protótipo: [SIJIA](https://sijia-gustavo-b017s-projects.vercel.app/)")

st.write("")

col1, col2 = st.columns([0.5,0.5])

col1.video("https://youtu.be/5zhn5S85j0Q")
col2.video("https://youtu.be/uZpetHS-DDY?si=wU4-JoBYERgDRiZU")









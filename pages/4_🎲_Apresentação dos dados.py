import streamlit as st
import plotly.graph_objects as go
from plotnine import *

# Configuração da página
st.set_page_config(page_title="Análise de Dados", layout="wide")

# Adicionando o logo
st.logo("logo_google.png")

# Criando as sub-abas (pages)
pages = st.sidebar.selectbox("Escolha um tópico:", [
    "Introdução",
    "Classificação das Variavies",
    "Perguntas-Chave"
])

st.sidebar.markdown("Desenvolvido por Gilson Dias [Linkedin](https://www.linkedin.com/in/gilson-dias-jn/) [GitHub](https://github.com/G1lsJn)")

# Função para exibir gráfico Plotly
def plot_distribution(x, y, title, xlabel, ylabel):
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
    st.plotly_chart(fig)

# Introdução
if pages == "Introdução":
    st.header("Análise de Dados sobre Adoção de Tecnologias Digitais nas Industrias")

    st.write("""
             A crescente digitalização das empresas tem sido um tema central no cenário industrial, 
             impactando a produtividade, competitividade e inovação. Diante disso, escolhi estudar esses 
             dados para compreender melhor como a adoção de tecnologias digitais se distribui entre diferentes 
             setores e quais padrões emergem dessa transformação tecnológica. Meu objetivo é identificar tendências, possíveis lacunas na implementação de inovações e entender quais fatores podem estar influenciando a decisão das empresas em adotar ou não tecnologias como Inteligência Artificial (IA), Big Data, Computação em Nuvem, Internet das Coisas (IoT) e Robótica.
             
             Além disso, minha motivação para essa análise está diretamente ligada ao meu interesse em trabalhar 
             com o desenvolvimento de software na Google. Por isso, busquei entender melhor a aceitação dos 
             softwares no mercado industrial, identificando quais tecnologias estão sendo adotadas e quais 
             desafios ainda precisam ser superados. Essa investigação pode fornecer insights importantes sobre 
             o impacto das soluções tecnológicas no setor e como elas podem ser aprimoradas para melhor atender 
             às demandas do mercado.

             Este relatório apresenta uma análise detalhada dos dados disponíveis, buscando responder questões 
             fundamentais sobre a adoção dessas tecnologias. Para isso, serão calculadas medidas centrais (média, 
             mediana e moda), além de métricas de dispersão como desvio padrão e variância. Também será explorada 
             a correlação entre variáveis e aplicadas distribuições probabilísticas para modelar o comportamento 
             da adoção tecnológica.
             """)
    
    df = st.session_state["data"]

    st.write("### Tabela de Dados usados:")
    st.write(df)

    st.write("*Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Estatísticas Estruturais e Temáticas em Empresas, Pesquisa de Inovação Semestral 2022. [Pesquisa de Inovação Semestral - PINTEC Semestral](https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/35867-pesquisa-de-inovacao-semestral.html?edicao=37966&t=resultados)* ")

# Classificação das variaveis
elif pages == "Classificação das Variavies":
    st.header("Classificação das Variáveis do Conjunto de Dados")
    
    st.write("""
        Os dados fornecidos representam o uso de tecnologias digitais por setores industriais. 
        Para realizar uma análise estatística rigorosa, é essencial classificar corretamente as 
        variáveis presentes. Abaixo, apresentamos essa classificação
    """)

    st.write("""
        ### Setor Industrial
        * Representa os diferentes setores da indústria que estão sendo analisados, como "Fabricação de produtos alimentícios" ou "Confecção de artigos do vestuário e acessórios". \n
            *Tipo:* **Categórica Nominal** (não possui uma ordem lógica) \n
            *Aplicação:* Permite segmentar a análise para verificar quais setores adotam mais ou menos tecnologias.
    """)

    st.divider()

    st.write("""
        ### ID_Empresa
        * Numeração única para cada setor industrial. \n
            *Tipo:* Numérica Discreta (usada apenas como identificador).
         """)
    
    st.divider()
    
    st.write("""
        ### Demais variaveis 
        As demais variáveis indicam a quantidade de empresas que adotam ou não determinadas tecnologias e, portanto, são **numéricas discretas**. São elas:

        * **Número de empresas:** Total de empresas no setor analisado.
        * **Utilizam tecnologia digital:** Número de empresas que adotam tecnologias digitais em seus processos. 
        * **Utilizam análise de big data / Não utilizam big data:** Empresas que utilizam ou não técnicas de análise de big data. 
        * **Utilizam computação em nuvem / Não utilizam computação em nuvem:** Empresas que adotam ou não computação em nuvem. 
        * **Utilizam IA / Não utilizam IA:** Empresas que adotam ou não Inteligência Artificial.
        * **Utilizam IoT / Não utilizam IoT:** Empresas que adotam ou não Internet das Coisas. 
        * **Utilizam Robótica / Não utilizam Robótica:** Empresas que utilizam ou não automação robótica.
        
            *Tipo Estatístico:* Numérica Discreta. \n
            *Aplicação:* Essas variáveis são fundamentais para calcular estatísticas descritivas, medir tendências de adoção tecnológica e identificar padrões.
             
       
""")

# Perguntas-Chave
elif pages == "Perguntas-Chave":

    st.write("""
        # Perguntas-Chave
             
        * Quais setores industriais utilizam mais tecnologia digital?
        * Qual a relação entre o uso de big data, computação em nuvem e IA nos setores?
        * Quais setores apresentam maior resistência ao uso de novas tecnologias?
        * Existe correlação entre a quantidade de empresas e a adoção de tecnologia?
        * Há setores que adotam predominantemente uma tecnologia específica?
        """)
    
    st.write(" ")
    st.write(" ")
    st.write(" ")
    
    st.image("pergunta.png")
    
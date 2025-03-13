import streamlit as st
import numpy as np
import scipy.stats as stats
import plotly.graph_objects as go
from plotnine import *
import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Aplicação de Distribuições Probabilísticas", layout="wide")

# Carregando data
df = st.session_state["data"]

# Adicionando o logo
st.logo("logo_google.png")


st.sidebar.markdown("Desenvolvido por Gilson Dias [Linkedin](https://www.linkedin.com/in/gilson-dias-jn/) [GitHub](https://github.com/G1lsJn)")

# Título da aplicação
st.title("📊 Análise de Distribuições Probabilísticas")


    # Exibir os primeiros registros
st.write("### Prévia dos Dados")
st.dataframe(df.head())

# Seleção das colunas para análise
colunas_disponiveis = df.columns.tolist()
    
coluna_normal = st.selectbox("Selecione a variável para a Distribuição Normal", colunas_disponiveis)
coluna_poisson = st.selectbox("Selecione a variável para a Distribuição de Poisson", colunas_disponiveis)

if coluna_normal and coluna_poisson:
    # Filtrando os dados
    data_normal = df[coluna_normal].dropna()
    data_poisson = df[coluna_poisson].dropna()

    # Garantindo que os dados são numéricos
    data_normal = pd.to_numeric(data_normal, errors='coerce').dropna()
    data_poisson = pd.to_numeric(data_poisson, errors='coerce').dropna()

    if not data_normal.empty and not data_poisson.empty:
        # Ajuste à Distribuição Normal
        mu, sigma = np.mean(data_normal), np.std(data_normal)
        x = np.linspace(min(data_normal), max(data_normal), 100)
        pdf = stats.norm.pdf(x, mu, sigma)

        # Ajuste à Distribuição de Poisson
        lambda_poisson = np.mean(data_poisson)
        poisson_x = np.arange(0, max(data_poisson) + 1)
        poisson_pmf = stats.poisson.pmf(poisson_x, lambda_poisson)

        # Criando gráficos
        fig, ax = plt.subplots(1, 2, figsize=(14, 6))

        # Gráfico da Distribuição Normal
        sns.histplot(data_normal, kde=True, bins=20, ax=ax[0], color='skyblue', stat='density')
        ax[0].plot(x, pdf, 'r', label='Distribuição Normal')
        ax[0].set_title(f"Ajuste à Distribuição Normal ({coluna_normal})")
        ax[0].legend()

            # Gráfico da Distribuição de Poisson
        sns.histplot(data_poisson, bins=20, discrete=True, ax=ax[1], color='orange', stat='density')
        ax[1].stem(poisson_x, poisson_pmf, linefmt='r-', markerfmt='ro', basefmt=" ")
        ax[1].set_title(f"Ajuste à Distribuição de Poisson ({coluna_poisson})")
        ax[1].legend(["Distribuição de Poisson", "Dados Reais"])

            # Exibir gráficos no Streamlit
        st.pyplot(fig)

            # Análise e Conclusões
        st.write("## 📌 Conclusões")
        st.write("""
            - A distribuição Normal se ajusta bem aos dados de adoção de tecnologia digital, indicando que a maioria das empresas segue um comportamento previsível em relação à média.
            - A distribuição de Poisson apresenta discrepâncias em relação aos dados reais, sugerindo que a adoção de IA não ocorre de forma completamente aleatória, mas pode ser influenciada por fatores externos.
            - Recomenda-se testar outras distribuições como Exponencial ou Gama para modelar melhor a adoção de tecnologias inovadoras.
            """)
        
        
        st.write("## 📌 Escolha das Distribuições")

        st.write("""
                * **Distribuição Normal**: Será aplicada à variável "Utilizam tecnologia digital", pois essa distribuição é adequada para modelar fenômenos que apresentam uma média bem definida e dispersão simétrica ao redor dela.
                * **Distribuição de Poisson**: Será usada na variável "Utilizam IA", pois pode modelar a contagem de eventos discretos, como a quantidade de empresas adotando IA em um setor específico.
                """)
        
        st.write("### Distribuição Normal (Com relação aos que Utilizam tecnologia digital):")

        st.write("""
                * A variável "Utilizam tecnologia digital" segue razoavelmente um padrão normal, com a maioria dos valores concentrados próximos à média.
                * Pequenas discrepâncias podem ser explicadas por setores que adotam a tecnologia de maneira diferente.
                * Essa distribuição pode ser útil para prever a adoção tecnológica em setores similares.
        """)

        st.write("### Distribuição de Poisson (Com relação aos que Utilizam IA):")

        st.write("""
                * A variável "Utilizam IA" não se ajusta perfeitamente à distribuição de Poisson, pois há maior variação nos dados do que o esperado.
                * Isso pode indicar que a adoção de IA não ocorre de maneira puramente aleatória, sendo influenciada por políticas do setor ou investimentos específicos.
                * Apesar disso, a modelagem de Poisson ainda pode ser útil para prever a frequência de adoção em setores específicos.
        """)

    else:
        st.error("As colunas selecionadas não possuem dados numéricos suficientes para a análise.")
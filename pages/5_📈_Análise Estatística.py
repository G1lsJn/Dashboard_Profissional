import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotnine import *

# Configuração da página
st.set_page_config(page_title="Análise de Dados", layout="wide")

# Adicionando o logo
st.logo("logo_google.png")

# Carregando data
df = st.session_state["data"]


st.sidebar.markdown("Desenvolvido por Gilson Dias [Linkedin](https://www.linkedin.com/in/gilson-dias-jn/) [GitHub](https://github.com/G1lsJn)")

st.title("📌 Análise Estatística")

st.write("## 1.1 Medidas Centrais")
st.write("Média, Mediana e Moda foram calculadas para todas as variáveis relevantes. Os resultados estão apresentados na tabela abaixo:")
    
# Exibir tabela no Streamlit
st.write("#### Tabela e gráfico de Medidas Centrais")

# Calcular média, mediana e moda
medias = df.mean(numeric_only=True)
medianas = df.median(numeric_only=True)
modas = df.mode(numeric_only=True).iloc[0]  # Pega a primeira moda caso haja múltiplas

# Criar uma tabela com os resultados
medidas_centrais = pd.DataFrame({
    "Média": medias,
    "Mediana": medianas,
    "Moda": modas
})

fig, ax = plt.subplots(figsize=(12, 6))
medidas_centrais.plot(kind="bar", ax=ax)
ax.set_title("Média, Mediana e Moda das Variáveis Principais")
ax.set_ylabel("Valor")
ax.set_xlabel("Variáveis")
ax.set_xticklabels(medidas_centrais.index, rotation=45)
ax.grid(axis="y", linestyle="--", alpha=0.7)
ax.legend(title="Medidas")

c1, c2 = st.columns([0.4,0.6])

# Exibir a tabela e gráfico 
c1.write(medidas_centrais)
c1.write(" ")
c1.write("Média, Mediana e Moda foram calculadas para todas as variáveis relevantes e observou-se que a média de adoção de tecnologias varia significativamente entre setores.")

c2.pyplot(fig)

st.divider()

st.write("## 1.2 Dispersão dos Dados")

st.write("#### Tabela e Gráfico de Dispersão dos Dados")

# Calcular desvio padrão e variância
desvio_padrao = df.std(numeric_only=True)
variancia = df.var(numeric_only=True)

# Criar DataFrame com os resultados
dispersao_df = pd.DataFrame({"Desvio Padrão": desvio_padrao, "Variância": variancia})


# Criar gráfico de dispersão
fig, ax = plt.subplots(figsize=(12, 6))
dispersao_df.plot(kind="bar", ax=ax)
plt.title("Desvio Padrão e Variância das Variáveis")
plt.ylabel("Valor")
plt.xlabel("Variáveis")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.legend(title="Métricas")

c1, c2 = st.columns([0.4,0.6])

# Exibir a tabela e gráfico 
c1.dataframe(dispersao_df)
c2.pyplot(fig)

c1.write("""
        * Desvio padrão e variância indicam grande variação no número de empresas por setor, o que sugere que alguns setores possuem uma adoção de tecnologia significativamente maior do que outros.
        * Algumas variáveis apresentam caudas longas, indicando a presença de outliers. Esses valores discrepantes podem indicar setores altamente especializados ou inconsistências na coleta de dados.
        """)



st.divider()

st.write("## 1.3 Distribuição dos Dados")

# Criar histogramas e boxplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# Histograma
df.hist(ax=axes[0, 0], bins=20, color='skyblue', edgecolor='black')
axes[0, 0].set_title("Distribuição das Variáveis")

# Boxplot
sns.boxplot(data=df, ax=axes[0, 1])
axes[0, 1].set_title("Boxplots das Variáveis")

# Exibir gráficos no Streamlit
st.pyplot(fig)

st.write("""
        * Histogramas revelaram distribuições assimétricas para a maioria das variáveis, indicando que a adoção de tecnologia não é uniforme entre os setores.
        * Boxplots demonstraram a presença de valores extremos, o que reforça a necessidade de um tratamento adequado para evitar que esses outliers distorçam análises futuras.
""")


st.divider()

st.title("📌 Correlação entre Variáveis")

st.write("""
        * Uma matriz de correlação foi gerada para identificar padrões entre as tecnologias utilizadas. A matriz revelou relações significativas entre diferentes variáveis, destacando quais tecnologias são adotadas conjuntamente em setores industriais.
        * Foi observada uma forte correlação positiva entre tecnologia digital, big data, computação em nuvem e IA, sugerindo que setores que adotam uma dessas tecnologias tendem a adotar as outras também.
        * A análise foi realizada utilizando o coeficiente de correlação de Pearson, que mede a relação linear entre duas variáveis. Valores próximos de 1 indicam uma correlação positiva forte, enquanto valores próximos de -1 indicam uma correlação negativa forte.
        * A tabela abaixo apresenta os coeficientes de correlação entre as principais variáveis:

""")


# Gerar matriz de correlação
correlacao = df.corr(numeric_only=True)

# Exibir matriz de correlação no Streamlit
st.write("### Matriz de Correlação entre Tecnologias")
st.dataframe(correlacao)

# Criar heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
plt.title("Heatmap da Matriz de Correlação")

# Exibir heatmap no Streamlit
st.pyplot(fig)

st.write("""
        * O heatmap da matriz de correlação acima destaca visualmente quais tecnologias têm maior relação entre si.
        * Setores que adotam big data e computação em nuvem frequentemente adotam IA, indicando uma possível dependência tecnológica entre essas áreas.
        * Baixa correlação foi encontrada entre robótica e outras tecnologias digitais, sugerindo que sua adoção pode ser mais independente ou baseada em necessidades específicas dos setores.
        """)

st.divider()

st.title("📌 Identificação de Outliers")

st.write("""
    Foram detectados valores extremos em setores específicos:

    * Maior número de empresas no Setor de produtos alimentícios: 1654
    * Maior uso de tecnologia digital no Setor de produtos alimentícios: 1418,55
    * Maior uso de big data no Setor de produtos alimentícios: 395,96
    * Maior uso de computação em nuvem no Setor de produtos alimentícios: 1263,94
    * Maior uso de IA no Setor de produtos alimentícios: 205,52
    * Maior uso de IoT no Setor de produtos alimentícios: 705,99 \n

    A análise desses valores sugere que todos esses outliers pertencem ao setor de produtos alimentícios. Esse setor possui o maior número de empresas, o que pode explicar a presença de valores extremos no uso de tecnologias. 
    A alta quantidade de empresas pode indicar um setor altamente tecnologizado, uma vez que a grande amostra favorece a adoção de múltiplas inovações. 
    No entanto, esses outliers também podem representar inconsistências nos dados, pois um setor com poucas empresas, mesmo que tenha uma alta taxa de adoção de tecnologia, dificilmente alcançará valores extremos como os observados no setor de produtos alimentícios.
    Portanto, é essencial investigar mais detalhadamente se esses valores refletem uma realidade setorial ou possíveis distorções nos dados coletados.
    """)

st.divider()

st.title("📌 Tendências Observadas")

st.write("""
        * Setores com maior número de empresas tendem a adotar mais tecnologias, o que pode ser explicado pelo maior acesso a recursos e necessidade de competitividade.
        * A presença de outliers nos dados sugere que o setor de produtos alimentícios é um dos mais tecnologizados, pois concentra um grande número de empresas, refletindo uma maior adoção tecnológica.
        * O uso de IA e robótica ainda é menor comparado a outras tecnologias, possivelmente devido ao alto custo de implementação e complexidade técnica.
        * Mesmo que um setor com poucas empresas apresente uma alta taxa de adoção de tecnologia, seus valores absolutos dificilmente alcançam os extremos observados no setor de produtos alimentícios.
        * Esses dados indicam que setores com maior base industrial podem se tornar polos de inovação tecnológica, enquanto setores menores podem precisar de incentivos para adoção mais ampla de novas tecnologias.
        * Para confirmar essas tendências, recomenda-se aprofundar a análise considerando fatores como faturamento, tamanho médio das empresas e políticas de inovação específicas para cada setor.
""")




import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def carregar_dados():
    merged_df = pd.read_csv("sustentabilidade_agricola_brasil_IEEA_2023.csv")
    merged_df = merged_df.sort_values(by="IEEA_Normalizado", ascending=False)
    return merged_df

merged_df = carregar_dados()

st.set_page_config(page_title="Dashboard Agrícola - Sustentabilidade e Eficiência", layout="wide")

st.title("Dashboard da Eficiência e Sustentabilidade Agrícola - Brasil 2023")
st.markdown("""
Este painel apresenta uma visão integrada da eficiência agrícola e sustentabilidade ambiental nos estados brasileiros.
Aqui é possível explorar como o equilíbrio entre produtividade, economia e meio ambiente se manifesta na prática.
""")

abas = st.tabs(["Sustentabilidade Ambiental", "Eficiência Produtiva", "Desempenho Econômico"])

with abas[0]:
    st.header("Sustentabilidade Ambiental")

    st.markdown("""
    O Índice de Eficiência Ecológica Agrícola (IEEA) combina fatores de sustentabilidade (ISA),
    PIB agropecuário e impacto ambiental (emissões e desmatamento).
    Quanto maior o IEEA, mais eficiente e sustentável é a produção agrícola do estado.
    """)

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(x="IEEA_Normalizado", y="Estado", data=merged_df, palette="YlGn", ax=ax)
    ax.set_title("Ranking de Eficiência Ecológica Agrícola (IEEA) - 2023")
    ax.set_xlabel("IEEA Normalizado (0–100)")
    ax.set_ylabel("Estado")
    st.pyplot(fig)

    st.markdown("""
    Estados com alto IEEA conseguem equilibrar produtividade e sustentabilidade,
    enquanto os mais baixos ainda enfrentam desafios ambientais e estruturais.
    """)

    st.subheader("Desmatamento e Emissões de CO₂")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x="Area_Desmatada_ha", y="Emissoes_CO2_ton", hue="Regiao", data=merged_df, s=100, ax=ax)
    ax.set_title("Correlação entre Desmatamento e Emissões de CO₂")
    ax.set_xlabel("Área Desmatada (ha)")
    ax.set_ylabel("Emissões de CO₂ (ton)")
    st.pyplot(fig)

    st.markdown("""
    Há uma relação direta: quanto maior o desmatamento, maiores as emissões de CO₂.
    Estados que fogem dessa tendência indicam avanços tecnológicos e boas práticas ambientais.
    """)

with abas[1]:
    st.header("Eficiência Produtiva")

    st.markdown("""
    A eficiência produtiva mostra como os recursos agrícolas são utilizados para gerar valor.
    A produtividade e a irrigação eficiente são indicadores de inovação e gestão responsável.
    """)

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(x="Produtividade_Agrícola_R_ha", y="Estado", data=merged_df, palette="Greens_r", ax=ax)
    ax.set_title("Produtividade Agrícola por Estado (R$/ha)")
    ax.set_xlabel("Produtividade (R$/ha)")
    ax.set_ylabel("Estado")
    st.pyplot(fig)

    st.markdown("""
    Estados com maior produtividade por hectare demonstram melhor aproveitamento tecnológico e
    maior valor agregado à produção agrícola.
    """)

    st.subheader("Uso e Eficiência da Irrigação")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x="Irrigacao_%", y="Irrigacao_Eficiente_%", hue="Regiao", data=merged_df, palette="Blues", s=100, ax=ax)
    ax.set_title("Relação entre Uso e Eficiência de Irrigação")
    ax.set_xlabel("Área Irrigada (%)")
    ax.set_ylabel("Irrigação Eficiente (%)")
    st.pyplot(fig)

    st.markdown("""
    Nem sempre mais irrigação significa mais eficiência.
    O ideal é fazer mais com menos água, usando técnicas como gotejamento e sensores inteligentes.
    """)

with abas[2]:
    st.header("Desempenho Econômico")

    st.markdown("""
    Aqui avaliamos o impacto econômico e social da agricultura, analisando o PIB agropecuário e o número de empregos gerados.
    Esses dados refletem o peso do agronegócio na economia de cada estado.
    """)

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(x="PIB_Agropecuario_R$", y="Estado", data=merged_df, palette="YlOrBr", ax=ax)
    ax.set_title("PIB Agropecuário por Estado (R$ bilhões)")
    ax.set_xlabel("PIB do Setor Agropecuário (R$)")
    ax.set_ylabel("Estado")
    st.pyplot(fig)

    st.markdown("""
    Estados com PIB agropecuário elevado tendem a ter maior infraestrutura e integração de cadeias produtivas.
    """)

    st.subheader("PIB Agropecuário x Emissões de CO₂")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x="PIB_Agropecuario_R$", y="Emissoes_CO2_ton", hue="Regiao", data=merged_df, palette="coolwarm", s=100, ax=ax)
    ax.set_title("Relação entre PIB Agropecuário e Emissões de CO₂")
    ax.set_xlabel("PIB Agropecuário (R$)")
    ax.set_ylabel("Emissões de CO₂ (ton)")
    st.pyplot(fig)

    st.markdown("""
    O gráfico mostra o equilíbrio entre crescimento e sustentabilidade.
    Alguns estados alcançam alto PIB com baixo impacto ambiental, o que indica eficiência ecológica real.
    """)

    st.subheader("Empregos no Setor Agropecuário")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(x="Empregos_Agropecuarios", y="Estado", data=merged_df, palette="crest", ax=ax)
    ax.set_title("Empregos no Setor Agropecuário por Estado")
    ax.set_xlabel("Número de Empregos")
    ax.set_ylabel("Estado")
    st.pyplot(fig)

    st.markdown("""
    Além dos resultados ambientais e econômicos, o agronegócio é um grande gerador de empregos e renda,
    sendo vital para o equilíbrio social das regiões agrícolas.
    """)

st.markdown("---")
st.markdown("Projeto desenvolvido por Victor Henrique — Dados e visualizações sobre sustentabilidade, eficiência e economia agrícola no Brasil.")
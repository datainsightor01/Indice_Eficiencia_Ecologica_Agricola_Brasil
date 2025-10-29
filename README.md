# 🌱 Dashboard de Eficiência e Sustentabilidade Agrícola do Brasil

Este projeto apresenta uma análise detalhada da **eficiência ecológica e produtiva da agricultura brasileira**, combinando fatores ambientais, econômicos e de produtividade.  
O objetivo é auxiliar pesquisadores, produtores e gestores públicos a compreender melhor o equilíbrio entre **crescimento agrícola e sustentabilidade ambiental**.

---

## 📊 Sobre o Projeto

O dashboard foi desenvolvido com **Python** e **Streamlit**, e utiliza dados relacionados à agricultura, emissões de carbono, desmatamento, PIB agropecuário e o **Índice de Sustentabilidade Agrícola (ISA)** para gerar o **IEEA (Índice de Eficiência Ecológica Agrícola)** — um novo indicador criado para medir a harmonia entre produtividade e impacto ambiental.

---

## 🌍 O que é o IEEA?

O **IEEA** é um índice que combina variáveis econômicas e ecológicas, expressando a eficiência agrícola considerando tanto **sustentabilidade quanto produção**.  

A fórmula utilizada é:

\[
IEEA = \frac{(ISA \times PIB_{Agropecuário})}{Emissões_{CO₂} + \frac{Área_{Desmatada}}{100}} \times 10^5
\]

O resultado é então **normalizado de 0 a 100**, permitindo comparação direta entre diferentes regiões e períodos.

---

## 📈 Principais Indicadores e Análises

O dashboard mostra diversos aspectos da agricultura brasileira, incluindo:

- **Eficiência Ecológica (IEEA)** por estado.  
- **Sustentabilidade (ISA)** e suas correlações com fatores ambientais.  
- **PIB Agropecuário** e produtividade por região.  
- **Emissões de CO₂** e **área desmatada**.  
- **Análises comparativas** entre eficiência, sustentabilidade e economia.

Os gráficos foram elaborados para serem **intuitivos, interativos e informativos**, permitindo ao usuário compreender rapidamente como os diferentes fatores se relacionam.

---

## 💻 Tecnologias Utilizadas

- **Python 3.11+**  
- **Pandas** — Manipulação e análise de dados  
- **Matplotlib / Seaborn** — Visualizações  
- **Streamlit** — Criação do dashboard interativo  

---

## 🧠 Insights Iniciais

- Estados com **altos valores de ISA** e **baixo desmatamento** tendem a apresentar **maior eficiência ecológica (IEEA)**.  
- Regiões com **PIB agropecuário elevado** mas **emissões de CO₂ crescentes** demonstram desequilíbrio na sustentabilidade.  
- A normalização do IEEA facilita comparações entre diferentes biomas e escalas produtivas.

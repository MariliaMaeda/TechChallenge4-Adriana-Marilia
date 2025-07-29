import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Painel de Obesidade", layout="wide")

# Carregar os dados traduzidos
@st.cache_data
def carregar_dados():
    return pd.read_csv("Obesidade_traduzido.csv")

df = carregar_dados()

# Cálculo do IMC
df["IMC"] = df["Peso (kg)"] / (df["Altura (m)"] ** 2)

# Título
st.title("Painel de Insights - Perfil de Obesidade")

st.markdown("""
Este painel apresenta uma visão interativa sobre o perfil dos pacientes com base em dados comportamentais, físicos e níveis de obesidade.
""")

# Filtros laterais
with st.sidebar:
    st.header("Filtros")
    nivel = st.multiselect("Nível de Obesidade:", df["Nível de Obesidade"].unique())
    genero = st.multiselect("Gênero:", df["Gênero"].unique())
    transporte = st.multiselect("Meio de Transporte:", df["Meio de Transporte"].unique())
    if nivel:
        df = df[df["Nível de Obesidade"].isin(nivel)]
    if genero:
        df = df[df["Gênero"].isin(genero)]
    if transporte:
        df = df[df["Meio de Transporte"].isin(transporte)]

# Indicadores principais
col1, col2, col3 = st.columns(3)
col1.metric("Total de Pacientes", len(df))
col2.metric("IMC Médio", round(df["IMC"].mean(), 2))
col3.metric("Idade Média", round(df["Idade"].mean(), 1))

# Gráfico: Distribuição dos níveis de obesidade
st.subheader("Distribuição dos Níveis de Obesidade")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.countplot(data=df, y="Nível de Obesidade", order=df["Nível de Obesidade"].value_counts().index, palette="viridis", ax=ax1)
ax1.set_xlabel("Número de Pacientes")
ax1.set_ylabel("Nível de Obesidade")
st.pyplot(fig1)

# Gráfico: IMC por nível de obesidade
st.subheader("Distribuição do IMC por Nível de Obesidade")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.boxplot(data=df, x="Nível de Obesidade", y="IMC", palette="viridis", ax=ax2)
ax2.set_xlabel("Nível de Obesidade")
ax2.set_ylabel("IMC")
plt.xticks(rotation=45)
st.pyplot(fig2)

# Gráfico: Consumo de Álcool por Nível
st.subheader("Consumo de Álcool por Nível de Obesidade")
fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.countplot(data=df, x="Consumo de Álcool", hue="Nível de Obesidade", palette="viridis", ax=ax3)
st.pyplot(fig3)

# Gráfico: Meio de Transporte por Nível
st.subheader("Meio de Transporte por Nível de Obesidade")
fig4, ax4 = plt.subplots(figsize=(10, 5))
sns.countplot(data=df, x="Meio de Transporte", hue="Nível de Obesidade", palette="viridis", ax=ax4)
plt.xticks(rotation=45)
st.pyplot(fig4)

# Gráfico: Lanches entre refeições por Nível
st.subheader("Lanches entre Refeições por Nível de Obesidade")
fig5, ax5 = plt.subplots(figsize=(10, 5))
sns.countplot(data=df, x="Lanches entre Refeições", hue="Nível de Obesidade", palette="viridis", ax=ax5)
st.pyplot(fig5)


# Gráfico: Histórico Familiar de Obesidade por Nível
st.subheader("Histórico Familiar de Obesidade por Nível de Obesidade")
fig7, ax7 = plt.subplots(figsize=(10, 5))
sns.countplot(data=df, x="Histórico Familiar de Obesidade", hue="Nível de Obesidade", palette="viridis", ax=ax7)
ax7.set_xlabel("Histórico Familiar de Obesidade (0 = Não, 1 = Sim)")
st.pyplot(fig7)

# Gráfico: Consumo de Alimentos Calóricos por Nível de Obesidade
st.subheader("Consumo de Alimentos Calóricos por Nível de Obesidade")
fig8, ax8 = plt.subplots(figsize=(10, 5))
sns.countplot(data=df, x="Consome Alimentos Calóricos", hue="Nível de Obesidade", palette="viridis", ax=ax8)
ax8.set_xlabel("Consome Alimentos Calóricos (0 = Não, 1 = Sim)")
st.pyplot(fig8)

# Gráfico: Hidratação Diária (litros) por Nível de Obesidade
st.subheader("Consumo Médio de Água por Nível de Obesidade")
fig9, ax9 = plt.subplots(figsize=(10, 5))
sns.barplot(data=df, x="Nível de Obesidade", y="Água Diária", palette="viridis", ax=ax9, errorbar="ci")
ax9.set_xlabel("Nível de Obesidade")
ax9.set_ylabel("Litros de Água por Dia")
plt.xticks(rotation=45)
st.pyplot(fig9)

# Gráfico: Frequência de Atividade Física por Nível de Obesidade
st.subheader("Atividade Física por Nível de Obesidade")
fig10, ax10 = plt.subplots(figsize=(10, 5))
sns.barplot(data=df, x="Nível de Obesidade", y="Frequência de Atividade Física", palette="viridis", ax=ax10, errorbar="ci")
ax10.set_xlabel("Nível de Obesidade")
ax10.set_ylabel("Frequência de Atividade Física (h/semana)")
plt.xticks(rotation=45)
st.pyplot(fig10)

# Rodapé
st.markdown("---")
st.caption("Desenvolvido para fins educacionais e apoio à triagem clínica.")
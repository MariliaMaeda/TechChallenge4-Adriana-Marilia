import streamlit as st
import pandas as pd
import joblib

# Carregar modelo e pré-processador
modelo = joblib.load("modelo_obesidade.pkl")
preprocessador = joblib.load("preprocessador.pkl")

st.set_page_config(page_title="Diagnóstico de Obesidade", layout="centered")

st.title("Avaliar Nível de Obesidade")
st.markdown("Informe os dados abaixo para avaliar o nível de obesidade.")

# Entradas do usuário
genero = st.selectbox("Gênero", ["Feminino", "Masculino"])
idade = st.number_input("Idade (anos)", min_value=0, max_value=100)
altura = st.number_input("Altura (em metros)", min_value=1.0, max_value=2.5, step=0.01)
peso = st.number_input("Peso (em kg)", min_value=30.0, max_value=250.0, step=0.1)
historico_familiar = st.selectbox("Histórico Familiar de Obesidade", ["Sim", "Não"])
alimentos_caloricos = st.selectbox("Consome Alimentos Calóricos com Frequência?", ["Sim", "Não"])
vegetais = st.slider("Frequência de Consumo de Vegetais (1 = nunca, 3 = sempre)", 1.0, 3.0, step=0.1)
refeicoes_dia = st.slider("Número de Refeições por Dia", 1.0, 4.0, step=0.5)
lanches = st.selectbox("Lanches entre Refeições", ["Nunca", "Pouco", "Frequentemente", "Sempre"])
fuma = st.selectbox("Fuma?", ["Sim", "Não"])
agua = st.slider("Consumo de Água Diário (litros)", 1.0, 3.0, step=0.1)
controla_calorias = st.selectbox("Controla a Ingestão de Calorias?", ["Sim", "Não"])
atividade_fisica = st.slider("Frequência de Atividade Física (0 = nenhuma, 1 = diária)", 0.0, 1.0, step=0.05)
tempo_tela = st.slider("Tempo de uso de dispositivos eletrônicos por dia (horas)", 0.0, 5.0, step=0.5)
alcool = st.selectbox("Consumo de Álcool", ["Nunca", "Pouco", "Frequentemente", "Sempre"])
transporte = st.selectbox("Meio de Transporte", ["Automóvel", "Bicicleta", "Motocicleta", "Transporte Público", "Caminhando", "Nunca"])

# Cálculo do IMC
imc = peso / (altura ** 2)

# Botão de previsão
if st.button("Avaliar Nível de Obesidade"):
    # Normalizar entradas para valores compatíveis com o modelo
    dados = pd.DataFrame([{
        'Gênero': 1 if genero == "Masculino" else 0,
        'Idade': idade,
        'Altura (m)': altura,
        'Peso (kg)': peso,
        'Histórico Familiar de Obesidade': 1 if historico_familiar == "Sim" else 0,
        'Consome Alimentos Calóricos': 1 if alimentos_caloricos == "Sim" else 0,
        'Consome Vegetais': vegetais,
        'Refeições por Dia': refeicoes_dia,
        'Lanches entre Refeições': lanches,
        'Fuma': 1 if fuma == "Sim" else 0,
        'Água Diária': agua,
        'Controla Calorias': 1 if controla_calorias == "Sim" else 0,
        'Frequência de Atividade Física': atividade_fisica,
        'Tempo com Dispositivos Eletrônicos': tempo_tela,
        'Consumo de Álcool': alcool,
        'Meio de Transporte': transporte,
        'IMC': imc
    }])

    # Aplicar o pré-processamento
    dados_transformados = preprocessador.transform(dados)
    if hasattr(dados_transformados, "toarray"):
        dados_transformados = dados_transformados.toarray()

    # Predição
    predicao = modelo.predict(dados_transformados)

    # Resultado
    st.success(f"O nível estimado de obesidade é: *{predicao[0]}*")
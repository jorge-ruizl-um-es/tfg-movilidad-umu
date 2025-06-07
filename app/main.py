import streamlit as st
import pandas as pd
import numpy as np
from src.emissions.model import estimate_emissions

st.set_page_config(page_title="Huella de carbono laboral", layout="wide")
st.title("🔍 Simulación de huella de carbono laboral")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/datos_movilidad_coordenadas.csv")
    return df.dropna(subset=["Distancia_km"])

df = load_data()

# Escenario configurable
porcentaje_bus = st.slider("% de personas que usan autobús en el escenario", 0, 100, 50)
df['Modo_Alternativo'] = df['Modo_Transporte']
df.loc[df.sample(frac=porcentaje_bus/100).index, 'Modo_Alternativo'] = 'bus'

# Recalcular emisiones
st.subheader("Resultados del escenario")
df['Emision_alternativa'] = df.apply(lambda row: estimate_emissions(row['Modo_Alternativo'], row['Distancia_km']) * 2 * 220, axis=1)
df['Reduccion_kg'] = df['Emision_anual_kgCO2'] - df['Emision_alternativa']

col1, col2 = st.columns(2)
with col1:
    st.metric("Emisión actual total (kg CO₂)", f"{df['Emision_anual_kgCO2'].sum():,.0f}")
with col2:
    st.metric("Emisión en escenario (kg CO₂)", f"{df['Emision_alternativa'].sum():,.0f}", delta=f"-{df['Reduccion_kg'].sum():,.0f}")

# Tabla de resultados
st.dataframe(df[['Nombre', 'Modo_Transporte', 'Modo_Alternativo', 'Distancia_km', 'Emision_anual_kgCO2', 'Emision_alternativa', 'Reduccion_kg']].sort_values(by='Reduccion_kg', ascending=False))

# Este archivo implementa una interfaz web interactiva en Streamlit para explorar cómo distintos porcentajes de uso del autobús afectan las emisiones totales de CO₂.


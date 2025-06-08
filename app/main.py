import streamlit as st
import pandas as pd
import numpy as np
from src.emissions.model import estimate_emissions

# Este archivo implementa una interfaz web interactiva en Streamlit para explorar cómo distintos porcentajes de uso del autobús afectan las emisiones totales de CO₂.

# Configuración de la página principal de la aplicación con streamlit
st.set_page_config(page_title="Huella de carbono laboral", layout="wide")
st.title("🔍 Simulación de huella de carbono laboral")

# Cargar datos
@st.cache_data
def load_data() -> pd.DataFrame:
    # De momento este CSV no existe
    df: pd.DataFrame = pd.read_csv("data/processed/datos_movilidad_coordenadas.csv")
    return df.dropna(subset=["Distancia_km"])

df = load_data()

# Escenario configurable
# Control deslizante interactivo para seleccionar un porcentaje (entre 0 y 100, iniciado a 50)
porcentaje_bus = st.slider("% de personas que usan autobús en el escenario", 0, 100, 50)

# Columna Modo_Alternativo en el df exactamente igual a Modo_Transporte
df['Modo_Alternativo'] = df['Modo_Transporte']

# Establece una proporción dada por el porcentaje de bus de filas al valor "bus" en la columna Modo_Alternativo
df.loc[df.sample(frac=porcentaje_bus/100).index, 'Modo_Alternativo'] = 'bus'

# Recalcular emisiones basándonos en el modo alternativo de transporte de cada instancia (fila), dependiendo de dicho medio
# y de la distancia recorrida.
st.subheader("Resultados del escenario")
df['Emision_alternativa'] = df.apply(lambda row: estimate_emissions(row['Modo_Alternativo'], row['Distancia_km']) * 2 * 220, axis=1)
df['Reduccion_kg'] = df['Emision_anual_kgCO2'] - df['Emision_alternativa']

# Dividir espacio horizontal de la interfaz gráfica de la aplicación en dos columnas
col1, col2 = st.columns(2)

# Mostrar los resultados calculados (a la izquierda la emisión actual, y a la derecha la emisión con la mejora propuesta)
with col1:
    st.metric("Emisión actual total (kg CO₂)", f"{df['Emision_anual_kgCO2'].sum():,.0f}")
with col2:
    st.metric("Emisión en escenario (kg CO₂)", f"{df['Emision_alternativa'].sum():,.0f}", delta=f"-{df['Reduccion_kg'].sum():,.0f}")
  
# Tabla de resultados - mostrar el dataframe de forma apropiada con la interfaz
st.dataframe(df[['Nombre', 'Modo_Transporte', 'Modo_Alternativo', 'Distancia_km', 'Emision_anual_kgCO2', 'Emision_alternativa', 'Reduccion_kg']].sort_values(by='Reduccion_kg', ascending=False))


import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#from datetime import time
st.title('Datos Hidrometereológicos Gobierno Regional Piura')
df = pd.read_csv('tb_medida_estaciones (1)_0.csv')
# Datos Hidrometereológicos Gobierno Regional Piura
st.title("Dashboard de Análisis de Datos")
# Mostrar el dataset en una tabla
st.subheader("Dataset")
st.dataframe(df)
# Mostrar un gráfico de línea con las columnas 13 y 14
st.subheader("Gráfico de Columnas 13 y 14")
st.line_chart(df[[13, 14]])

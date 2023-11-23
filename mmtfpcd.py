# -*- coding: utf-8 -*-
"""MMTFPCD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OFXrKpOIoeU2dYTtTTRpq3CTBT5_aak6

Trabajo Final
"""

# Instalar Streamlit
#!pip install streamlit

#Importar las librerías
#import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
import folium
import streamlit as st
#from streamlit_folium import st_folium
import geopandas as gpd
#from streamlit_folium import folium_static

df = pd.read_csv('tb_medida_estaciones (1)_0.csv')
df.shape

nansdf = df.isna().sum()

# Mostrar los valores NaN por columna
print(nansdf)

# cargar los datos del código de ubigeo
dfcu = pd.read_csv('TB_UBIGEOS.csv')
dfcu.shape

nansdfcu = dfcu.isna().sum()

dfcu_Piura = dfcu.loc[dfcu['departamento'] == 'PIURA']
dfcu_Piura
dfcu_Piura = dfcu_Piura.rename(columns={"ubigeo_inei": "UBIGEO"})

nansPiura = dfcu_Piura.isna().sum()
# Mostrar los valores NaN por columna
print(nansPiura)

# Realizar la fusión de los datasets utilizando el código de ubigeo como clave de relación
df_final = pd.merge(dfcu_Piura, df, left_on='UBIGEO', right_on='UBIGEO')

df_final.shape

nansdf_final = df_final.isna().sum()

# Crear una lista de opciones para la selección
opciones = df_final["ESTACION"].unique()

# Crear la barra lateral para seleccionar la característica
caracteristica = st.sidebar.selectbox("Selecciona una característica", opciones)

# Filtrar los datos según la característica seleccionada
df_finalf = df_final[df_final["ESTACION"] == caracteristica]

# Ordenar los datos según la columna "estación"
data_ordenada = df_finalf.sort_values(by="ESTACION")

# Mostrar la tabla ordenada
st.write(data_ordenada)
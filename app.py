import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón para construir un histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)


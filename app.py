import pandas as pd
import plotly.graph_objects as go 
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.title('Anaálisis de datos de anuncios de venta de coches usados en USA')

hist_button = st.button('Construir histograma')

if hist_button:

    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    fig.update_layout(title_text='Distribución del Odómetro')

    st.plotly_chart(fig, use_container_width=True)
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig2 = go.Figure(data=go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers'
    ))
    fig2.update_layout(title='Relación entre odómetro y precio')
    st.plotly_chart(fig2, use_container_width=True)
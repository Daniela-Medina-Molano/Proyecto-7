import streamlit as st
import pandas as pd
import plotly.graph_objects as go
st.title("Análisis Exploratorio de Vehículos")
st.header("Explora los datos de anuncios de autos usados en EE. UU.")
car_data = pd.read_csv('C:\\Users\\danie\\Proyecto-7\\vehicles_us.csv')
st.subheader("Datos de Vehículos")
st.write(car_data.head())
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)
disp_button = st.button('Construir gráfico de dispersión')
if disp_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=go.Scatter(x=car_data['price'], y=car_data['odometer'], mode='markers'))
    fig.update_layout(title_text='Precio vs Odómetro', xaxis_title='Precio', yaxis_title='Odómetro')
    st.plotly_chart(fig, use_container_width=True)
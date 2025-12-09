import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Vehículos",
    page_icon="🚗",
    layout="wide"
)

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')


# Título principal y descripción
st.title('🚗 Análisis de Datos de Vehículos')
st.markdown("""
Esta aplicación te permite explorar y analizar datos de vehículos usados.
Puedes filtrar por año y precio, y crear diferentes tipos de gráficos para entender mejor los datos.
""")

# Mostrar información básica de los datos
st.subheader('📊 Información del Dataset')
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de vehículos", len(car_data))
with col2:
    st.metric("Año más antiguo", int(car_data['model_year'].min()))
with col3:
    st.metric("Año más reciente", int(car_data['model_year'].max()))
# Verificar que los datos se cargaron
st.write(f"Datos cargados: {len(car_data)} filas")
st.write("Primeras 5 filas:")
st.write(car_data.head())

# Título de la aplicación
st.header('Análisis de Datos de Vehículos')


# Agregar un slider para filtrar por año
year_range = st.slider(
    'Selecciona el rango de años',
    min_value=int(car_data['model_year'].min()),
    max_value=int(car_data['model_year'].max()),
    value=(int(car_data['model_year'].min()), int(car_data['model_year'].max()))
)

# Filtrar los datos basado en el slider
filtered_data = car_data[
    (car_data['model_year'] >= year_range[0]) & 
    (car_data['model_year'] <= year_range[1])
]

# Slider para rango de precios
price_range = st.slider(
    'Selecciona el rango de precios',
    min_value=int(car_data['price'].min()),
    max_value=int(car_data['price'].max()),
    value=(int(car_data['price'].min()), int(car_data['price'].max())),
    step=1000
)

# Filtrar los datos basado en AMBOS sliders
filtered_data = car_data[
    (car_data['model_year'] >= year_range[0]) & 
    (car_data['model_year'] <= year_range[1]) &
    (car_data['price'] >= price_range[0]) & 
    (car_data['price'] <= price_range[1])
]

# Botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creando un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma
    fig = px.histogram(filtered_data, x="odometer", nbins=50)

     # Mostrar el gráfico (ESTA LÍNEA FALTA)
    st.plotly_chart(fig, use_container_width=True)

    # Botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creando un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el gráfico de dispersión
    fig = px.scatter(filtered_data, x="odometer", y="price")
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)

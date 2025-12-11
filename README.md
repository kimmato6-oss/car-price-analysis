# Car Price Analysis

Este proyecto forma parte de un ejercicio académico para practicar
Python, web scraping, análisis de datos y despliegue de aplicaciones
web. El objetivo principal es extraer información de precios de un sitio
web, procesarla, analizarla y presentarla en una aplicación sencilla
desplegada en Render.

------------------------------------------------------------------------

## 1. Objetivo del proyecto

El propósito del proyecto es:

-   Extraer datos de productos desde una página web utilizando **web
    scraping** con `requests` y `BeautifulSoup`.
-   Procesar los datos obtenidos y estructurarlos en un **DataFrame de
    pandas**.
-   Realizar análisis exploratorios básicos.
-   Desplegar una **aplicación web en Render** que permita visualizar el
    análisis.

------------------------------------------------------------------------

## 2. Estructura del repositorio

    car-price-analysis/
    │── app.py                # Aplicación principal desplegada en Render
    │── data/                 # Datos generados o procesados (si aplica)
    │── README.md             # Documentación del proyecto
    │── requirements.txt      # Lista de dependencias
    └── assets/               # Imágenes u otros elementos opcionales

------------------------------------------------------------------------

## 3. Tecnologías utilizadas

-   **Python 3**
-   **requests**
-   **BeautifulSoup4**
-   **pandas**
-   **Flask / Streamlit** (dependiendo de la implementación del app.py)
-   **Render** para el despliegue de la aplicación

------------------------------------------------------------------------

## 4. Instalación y ejecución local

### Requisitos previos

Asegúrate de tener instalado:

-   Python 3.8 o superior
-   pip

### Pasos

1.  Clona el repositorio:

``` bash
git clone https://github.com/kimmato6-oss/car-price-analysis.git
```

2.  Entra en la carpeta del proyecto:

``` bash
cd car-price-analysis
```

3.  Instala las dependencias:

``` bash
pip install -r requirements.txt
```

4.  Ejecuta la aplicación localmente:

``` bash
python app.py
```

La aplicación se ejecutará normalmente en:

    http://localhost:5000

------------------------------------------------------------------------

## 5. Despliegue en Render

Este proyecto está desplegado en:

**https://car-price-analysis-irzb.onrender.com**

Render detecta automáticamente `app.py` como punto de entrada y utiliza
`requirements.txt` para instalar las dependencias.

------------------------------------------------------------------------

## 6. Web Scraping realizado

El proyecto extrae la información desde:

**https://tripleten-com.github.io/simple-shop_es/**

Se obtienen:

-   Nombres de los productos\
-   Precios

Código utilizado para el scrap:

``` python
import requests
from bs4 import BeautifulSoup

URL = 'https://tripleten-com.github.io/simple-shop_es/'
req = requests.get(URL)
soup = BeautifulSoup(req.text, 'lxml')

name_products = []
for row in soup.find_all('p', attrs={'class': 't754__title t-name t-name_md js-product-name'}):
    name_products.append(row.text)

price = []
for row in soup.find_all('p', attrs={'class': 't754__price-value js-product-price'}):
    price.append(row.text)
```

Luego se construye el DataFrame:

``` python
import pandas as pd

df = pd.DataFrame({'name': name_products, 'price': price})
print(df.head())
```

------------------------------------------------------------------------

## 7. Resultados principales

-   Se obtiene una tabla limpia con nombres y precios.
-   Los datos pueden ser analizados y visualizados desde la aplicación
    desplegada.
-   El proyecto permite practicar web scraping y desarrollo de apps
    simples.

------------------------------------------------------------------------

## 8. Autor

**Kimberly Juliana Marles Torres**\
Proyecto académico -- TripleTen

------------------------------------------------------------------------

## 9. Licencia

Este proyecto es de uso académico y libre para consulta.
cd 
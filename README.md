# Mapa Interactivo de Resultados Electorales en Uruguay

Este proyecto genera un mapa interactivo que permite visualizar los resultados de las elecciones en Uruguay, comparando los datos de 2019 y 2024. El mapa destaca los municipios donde los partidos ganaron o perdieron apoyo, así como las variaciones más significativas en los votos.

El archivo principal generado es `resultados_electorales_uruguay.html`, que contiene el mapa interactivo.

## Archivos del Proyecto

- **`procesar_mapa.py`**  
  Convierte el shapefile de los municipios electorales en un archivo GeoJSON, necesario para la visualización del mapa.

- **`simplificar_mapa.py`**  
  Simplifica las geometrías del GeoJSON generado para mejorar el rendimiento del mapa.

- **`crear_mapa.py`**  
  Crea el archivo HTML (`resultados_electorales_uruguay.html`) con el mapa interactivo.

- **`resultados_electorales_uruguay.html`**  
  El mapa interactivo generado. Este es el resultado final y puede abrirse directamente en un navegador (recomendado usar Google Chrome).

## Requisitos

Antes de comenzar, asegúrate de instalar las dependencias necesarias ejecutando:  
```bash
pip install -r requirements.txt



# Interactive Map of Electoral Results in Uruguay

This project generates an interactive map that visualizes the election results in Uruguay, comparing data from 2019 and 2024. The map highlights municipalities where parties gained or lost support, as well as the most significant vote variations.

The main output file is `resultados_electorales_uruguay.html`, which contains the interactive map.

## Project Files

- `procesar_mapa.py`: Converts the electoral municipalities' shapefile into a GeoJSON file, necessary for the map visualization.

- `simplificar_mapa.py`: Simplifies the geometries of the generated GeoJSON to improve map performance.

- `crear_mapa.py`: Creates the HTML file (`resultados_electorales_uruguay.html`) with the interactive map.

- `resultados_electorales_uruguay.html`: The generated interactive map. This is the final result and can be opened directly in a browser (recommended to use Google Chrome).

## Requirements

Before starting, make sure to install the necessary dependencies by running:  
```bash
pip install -r requirements.txt
```
---
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
```

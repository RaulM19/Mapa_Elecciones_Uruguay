import folium
import folium.map
import json
import pandas as pd
import geopandas as gpd
from utils import style_function_color_ganador_2019, style_function_color_ganador_2024, mapa_con_resultados , style_function_color_K_diferencia_N,style_function_color_K_diferencia_F , obtener_k_municipios_mayor_diferencia

# Ruta al archivo GeoJSON creado
geojson_path = "mapa_uruguay_simplificado.json"
geojson_data = mapa_con_resultados(geojson_path)

uruguay_bounds = [[-36.5, -60.0], [-28.5, -51.0]]  # Coordenadas aproximadas del país
# Crear mapa
mapa = folium.Map(
    location=[-32.0, -56.0],  # Coordenadas del centro de Uruguay
    zoom_start=7,
    min_zoom=6,  
    max_zoom=13,  
    maxBounds= uruguay_bounds,
    max_bounds=True
)
mapa.fit_bounds(uruguay_bounds)

# Agregar título al mapa
titulo_html = """
<div style="position: fixed; 
            top: 10px; left: 50%; transform: translateX(-50%);
            z-index: 1000; 
            background-color: white; 
            padding: 10px; 
            border: 2px solid black; 
            font-size: 20px;">
    <b>Resultados Electorales de Uruguay</b>
</div>
"""
mapa.get_root().html.add_child(folium.Element(titulo_html))

capa_ganador_2019 = folium.GeoJson(
    geojson_data,
    style_function=style_function_color_ganador_2019,
    tooltip=folium.GeoJsonTooltip(
        fields=["depto", "serie", "Partido Nacional 2019", "Frente Amplio 2019"],  
        aliases=["Departamento: ", "Serie:", "Partido Nacional: ", "Frente Amplio: "],  
        localize=True
    ),
    name="Partido Ganador 2019",
    show=False
)

capa_ganador_2024 = folium.GeoJson(
    geojson_data,
    style_function=style_function_color_ganador_2024,
    tooltip=folium.GeoJsonTooltip(
        fields=["depto", "serie", "Partido Nacional 2024", "Frente Amplio 2024"],  
        aliases=["Departamento: ", "Serie:", "Partido Nacional: ", "Frente Amplio: "],  
        localize=True
    ),
    name="Partido Ganador 2024"
)


K= 25 # Top municipios con mayor diferencia de votos
geojson_data=obtener_k_municipios_mayor_diferencia(geojson_data, K) 


capa_top_k_N = folium.GeoJson(
    geojson_data,
    style_function= style_function_color_K_diferencia_N,
    tooltip=folium.GeoJsonTooltip(
        fields=["depto", "Partido Nacional 2019", "Partido Nacional 2024","diferencia_votos_N"],
        aliases=["Departamento: ", "Votos 2019:" , "Votos 2024:", "Diferencia de Votos: "],
        localize=True
    ),
    name=f"Top {K} Municipios con Mayor Diferencia Partido Nacional",
    show=False
)

capa_top_k_F = folium.GeoJson(
    geojson_data,
    style_function= style_function_color_K_diferencia_F,
    tooltip=folium.GeoJsonTooltip(
        fields=["depto", "Frente Amplio 2019", "Frente Amplio 2024","diferencia_votos_F"],
        aliases=["Departamento: ","Votos 2019:" , "Votos 2024:", "Diferencia de Votos: "],
        localize=True
    ),
    name=f"Top {K} Municipios con Mayor Diferencia Frente Amplio",
    show=False
)


# Agregar ambas capas al mapa
capa_ganador_2024.add_to(mapa)
capa_ganador_2019.add_to(mapa)
capa_top_k_N.add_to(mapa)
capa_top_k_F.add_to(mapa)

# Crear un control de capas para alternar entre las capas
folium.LayerControl(position='topright', collapsed=False).add_to(mapa)



# Guardar el mapa 
mapa.save("resultados_electorales_uruguay.html")
print("Mapa generado: resultados_electorales_uruguay.html")
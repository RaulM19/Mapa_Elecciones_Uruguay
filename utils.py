import folium
import json
import pandas as pd
import geopandas as gpd


# Función de estilo basada en el partido ganador en 2019
def style_function_color_ganador_2019(feature):
    municipio = feature["properties"]["ogc_fid"]
    votos_partido_a = feature["properties"]["Partido Nacional 2019"]
    votos_partido_b = feature["properties"]["Frente Amplio 2019"]

    if pd.notna(votos_partido_a) and pd.notna(votos_partido_b) :
        if votos_partido_a > votos_partido_b:
            partido_ganador = "N" 
        else:
            partido_ganador = "F"
    else:
        partido_ganador = None

    if partido_ganador == "N":
        color = "#00FFFF"  # Celeste
    elif partido_ganador == "F":
        color = "#FF0000"  # Rojo
    else:
        color = "#808080"  # Gris para valores sin datos

    return {
        "fillColor": color,
        "color": "black",
        "weight": 1,   
        "fillOpacity": 0.7,
    }

# Función de estilo basada en el partido ganador en 2024
def style_function_color_ganador_2024(feature):
    municipio = feature["properties"]["ogc_fid"]
    votos_partido_a = feature["properties"]["Partido Nacional 2024"]
    votos_partido_b = feature["properties"]["Frente Amplio 2024"]

    if pd.notna(votos_partido_a) and pd.notna(votos_partido_b) :
        if votos_partido_a > votos_partido_b:
            partido_ganador = "N" 
        else:
            partido_ganador = "F"
    else:
        partido_ganador = None

    if partido_ganador == "N":
        color = "#00FFFF"  # Celeste
    elif partido_ganador == "F":
        color = "#FF0000"  # Rojo
    else:
        color = "#808080"  # Gris para valores sin datos

    return {
        "fillColor": color,
        "color": "black",
        "weight": 1,   
        "fillOpacity": 0.7,
    }

# Carga el mapa de del path geojson_path
def mapa_con_resultados(geojson_path) :

    geojson_data = gpd.read_file(geojson_path)
    # Votos de 2019
    datos2019 = pd.read_csv('2019/balotaje_2019.csv') 
    datos2019.drop(columns=['Total_Habilitados','Total_Anulados','Total_EN_Blanco'], inplace=True)
    datos2019.drop(columns=['Total_Votos_Emitidos','Total_Votos_NO_Observados','Total_Votos_Observados'], inplace=True)
    datos2019.drop(columns=['Departamento','CRV'], inplace=True)
    datos2019.rename(columns={'Total_Martinez_Villar':'Frente Amplio 2019', 'Total_Lacalle Pou_Argimon':'Partido Nacional 2019'}, inplace=True)
    datos2019 = datos2019.groupby('Serie', as_index=False).sum()
    datos2019 = separar_series_fusionadas(datos2019,'2019')
    # Agregar resultados por partido 
    geojson_data = geojson_data.merge(datos2019, left_on="serie", right_on="Serie", how="left")
    geojson_data.drop(columns=['Serie'], inplace=True)

    # Votos de 2024
    datos2024 = pd.read_csv('2024/balotaje_2024.csv') 
    datos2024.drop(columns=['TotalHabilitados','TotalAnulados','TotalEnBlanco'], inplace=True)
    datos2024.drop(columns=['TotalVotosEmitidos','TotalVotosNoObservados','TotalVotosObservados'], inplace=True)
    datos2024.drop(columns=['Departamento','CRV'], inplace=True)
    datos2024.rename(columns={'TotalOrsiCosse':'Frente Amplio 2024', 'TotalDelgadoRipoll':'Partido Nacional 2024'}, inplace=True)
    datos2024 = datos2024.groupby('Serie', as_index=False).sum()
    datos2024 = separar_series_fusionadas(datos2024,'2024')
    # Agregar resultados por partido 
    geojson_data = geojson_data.merge(datos2024, left_on="serie", right_on="Serie", how="left")
    geojson_data.drop(columns=['Serie'], inplace=True)
    

    return geojson_data


# Dividir las series fusionadas
def separar_series_fusionadas(df, anio):

    filas_fusionadas = df[df['Serie'].str.contains(' ', na=False)]
    
    nuevas_filas = []
    if anio =='2024':
        votos_columns = ['Frente Amplio 2024','Partido Nacional 2024']# or 'Frente Amplio 2019' or 'Partido Nacional 2019'
    else:
        votos_columns = ['Frente Amplio 2019','Partido Nacional 2019']# or 'Frente Amplio 2019' or 'Partido Nacional 2019'
        
    # Convertir las columnas de votos a numéricas, forzando errores a NaN
    df[votos_columns] = df[votos_columns].apply(pd.to_numeric, errors='coerce')

    # Iterar sobre las filas fusionadas
    for _, row in filas_fusionadas.iterrows():
        series_fusionada = row['Serie'].split() 
        votos_divididos = row[votos_columns] // 2
        
        for serie in series_fusionada:
            nueva_fila = row.copy()
            nueva_fila['Serie'] = serie  
            nueva_fila[votos_columns] = votos_divididos  
            nuevas_filas.append(nueva_fila)

    # Eliminar las filas originales con series fusionadas
    df_sin_fusionadas = df[~df['Serie'].str.contains(' ', na=False)]

    # Crear un nuevo DataFrame con las filas sin fusionar y las nuevas filas divididas
    df_nuevo = pd.concat([df_sin_fusionadas, pd.DataFrame(nuevas_filas)], ignore_index=True)
    
    return df_nuevo


# Funcion para colorear los municipios con mayor diferencia de votos del partido nacional
def style_function_color_K_diferencia_N(feature):
    mayor_dif=feature["properties"]["diferencia_votos_N"]
    if pd.notna(mayor_dif) :
        color = "#A11FEB"
    else:
        color= "#808080"

    return {
        "fillColor": color,
        "color": "black",
        "weight": 1,   
        "fillOpacity": 0.7,
    }

# Funcion para colorear los municipios con mayor diferencia de votos del frente amplio
def style_function_color_K_diferencia_F(feature):
    mayor_dif=feature["properties"]["diferencia_votos_F"]
    if pd.notna(mayor_dif) :
        color = "#A11FEB"
    else:
        color= "#808080"

    return {
        "fillColor": color,
        "color": "black",
        "weight": 1,   
        "fillOpacity": 0.7,
    }


# Función para obtener los K municipios con mayor diferencia
def obtener_k_municipios_mayor_diferencia(geojson_data, k):
    # Calcular la diferencia de votos
    geojson_data['diferencia_votos_N'] = abs(geojson_data['Partido Nacional 2024'] - geojson_data['Partido Nacional 2019'])
    geojson_data['diferencia_votos_F'] = abs(geojson_data['Frente Amplio 2024'] - geojson_data['Frente Amplio 2019'])
    municipios_top_k_N = geojson_data.sort_values(by="diferencia_votos_N", ascending=False)
    municipios_top_k_F = geojson_data.sort_values(by="diferencia_votos_F", ascending=False)

    # Me qudo con los K primeros
    municipios_top_k_N=municipios_top_k_N.head(k)
    municipios_top_k_F=municipios_top_k_F.head(k)
    
    # Uno las tablas
    municipios_top_k_N = municipios_top_k_N.drop(["depto","Partido Nacional 2024","Partido Nacional 2019", "Frente Amplio 2024","Frente Amplio 2019","diferencia_votos_F","geometry", "serie"],axis=1)
    municipios_top_k_F = municipios_top_k_F.drop(["depto","Partido Nacional 2024","Partido Nacional 2019", "Frente Amplio 2024","Frente Amplio 2019","diferencia_votos_N","geometry", "serie"],axis=1)
    geojson_data = geojson_data.drop(['diferencia_votos_N'],axis=1)
    geojson_data = geojson_data.drop(['diferencia_votos_F'],axis=1)
    geojson_data = geojson_data.merge(municipios_top_k_N, left_on="ogc_fid", right_on="ogc_fid", how="left")
    geojson_data = geojson_data.merge(municipios_top_k_F, left_on="ogc_fid", right_on="ogc_fid", how="left")
    return geojson_data




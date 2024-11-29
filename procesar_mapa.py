import geopandas as gpd

# Cargar el archivo de los Municipios
shapefile_path = 'series_electorales_20240523/series_electorales_20240523.shp'
gdf = gpd.read_file(shapefile_path)

# Convertir a GeoJSON 
geojson_path = "mapa_uruguay.json"
gdf.to_file(geojson_path, driver="GeoJSON")

print("Archivo convertido a GeoJSON:", geojson_path)


# En caso de que el mapa sea muy pesado, correr el archivo simplificar_mapa.py
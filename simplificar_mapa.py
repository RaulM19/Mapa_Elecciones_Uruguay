# En caso de que el mapa original posea una carga poligonal atla se recomienda aumentar el factor de tolerancia.
import geopandas as gpd

# Cargar el mapa
gdf = gpd.read_file("mapa_uruguay.json")

# A mayor tolerancia menor cantidad de poligonos 
gdf["geometry"] = gdf["geometry"].simplify(tolerance=0.004)

# Guardar el archivo simplificado
gdf.to_file("mapa_uruguay_simplificado.json", driver="GeoJSON")

print("Mapa simplificado")

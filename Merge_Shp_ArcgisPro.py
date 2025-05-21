import arcpy
import os

# Obtiene la ruta actual
ruta_actual = os.getcwd()

# Abre el proyecto de ArcGIS Pro
aprx = arcpy.mp.ArcGISProject("CURRENT")

# Obtiene una lista de todas las capas en el contenido
capas = aprx.listMaps()[0].listLayers()

# Itera a través de las capas y muestra sus nombres
for capa in capas:
    print(f"Capa: {capa.name}, Ruta Actual: {ruta_actual}")


# Establece la ruta de salida para el nuevo shapefile
ruta_salida = os.path.join(ruta_actual, "shp_merge.shp")

# Abre el proyecto de ArcGIS Pro
aprx = arcpy.mp.ArcGISProject("CURRENT")

# Obtiene una lista de todas las capas en el contenido
capas = aprx.listMaps()[0].listLayers()

# Crea una lista de rutas de las capas para usar en la función Merge
rutas_capas = [capa.dataSource for capa in capas]

# Realiza la fusión (unión) de las capas en un nuevo shapefile
arcpy.management.Merge(rutas_capas, ruta_salida)

# Añade el nuevo shapefile a la tabla de contenido (layers)
aprx = arcpy.mp.ArcGISProject("CURRENT")
mapa = aprx.listMaps()[0]
nueva_capa = arcpy.mp.LayerFile(ruta_salida)
mapa.addLayer(nueva_capa)

# Guarda el proyecto
aprx.save()

print(f"Se ha creado y agregado el shapefile 'shp_merge.shp' a la tabla de contenido.")

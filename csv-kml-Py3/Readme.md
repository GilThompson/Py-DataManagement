# KML Grid Generator from Plot Configuration

Este repositorio contiene un script en Python para generar un archivo `.kml` compatible con Google Earth. El script toma coordenadas geográficas (latitud y longitud) de dos esquinas de una parcela experimental y un archivo de configuración de parcelas (`.csv`) para generar una grilla de polígonos que representa cada unidad experimental (plot) como un `Placemark` en un archivo KML.

Este código es una adaptación del trabajo previo de Athena y Lorena, extendido para automatizar la creación de capas KML a partir de configuraciones de campo.

---

## 🎯 ¿Qué hace este código?

- Lee un archivo de configuración (`config.csv`) que define:
  - Tamaño de las parcelas (plots)
  - Distribución (número de filas/columnas)
  - Distancias entre parcelas
  - Columnas especiales con mayores distancias
- Toma dos puntos GPS (coordenadas geográficas) como referencia para delimitar el área
- Calcula los polígonos para cada parcela en grados decimales
- Exporta un archivo `output.kml` con:
  - Polígonos (parcela por parcela)
  - Puntos centrales de cada parcela
  - Puntos de referencia (esquinas)

---

## 📁 Estructura del Proyecto
project_folder/
│
├── main.py # Script principal
├── lib/
│ ├── csvfile.py # Manejo de archivos CSV de configuración y etiquetas
│ ├── xmlbuilder.py # Construcción del archivo KML/XML
│ └── timer.py # Utilidades de temporizador
├── input/
│ ├── config.csv # Archivo de configuración de parcelas (ver ejemplo)
│ └── labels.csv # Nombres de las parcelas (opcional)
└── output.kml # Archivo KML generado


---

## ⚙️ Requisitos del sistema

- Python ≥ 3.6
- No requiere bibliotecas externas aparte de la estándar, pero se recomienda crear un entorno virtual.

---

## 📤 Salida
output.kml: Archivo que contiene:

Una carpeta principal con polígonos por parcela

Una carpeta con puntos centrales de cada parcela

Una carpeta con los dos puntos de referencia (Punto 1 y Punto 2)

El archivo .kml puede abrirse directamente en Google Earth para visualización y revisión espacial.
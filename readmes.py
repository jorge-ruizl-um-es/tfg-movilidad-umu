import os

# Estructura de carpetas con descripciones específicas
folders_with_readmes = {
    "data/raw": "Datos originales sin procesar. Aquí se coloca el Excel histórico proporcionado por la organización.",
    "data/processed": "Datos transformados y enriquecidos (ej. CSV con coordenadas, GeoJSON, etc.).",
    "notebooks": "Cuadernos Jupyter para análisis exploratorio, cálculo de emisiones, visualización, etc.",
    "src/geo": "Código para georreferenciación, cálculo de distancias y manejo espacial.",
    "src/emissions": "Módulos para estimar la huella de carbono según distancias y modos de transporte.",
    "src/visualization": "Código para generar mapas, dashboards interactivos o gráficos estáticos.",
    "src/simulation": "Simuladores de movilidad (por ejemplo, simulación basada en agentes).",
    "app": "Aplicación web o dashboard interactivo para visualizar resultados y permitir interacción.",
    "docs": "Documentación técnica, informes y materiales de apoyo.",
    "tests": "Pruebas automáticas de los módulos del proyecto."
}

# Crear carpetas y README.md en cada una
for folder, readme_text in folders_with_readmes.items():
    os.makedirs(folder, exist_ok=True)
    readme_path = os.path.join(folder, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"# {folder}\n\n{readme_text}\n")

# README general del repositorio
readme_general = """# Proyecto: Análisis de movilidad laboral y huella de carbono

Este proyecto tiene como objetivo analizar los desplazamientos laborales de una organización, calcular su huella de carbono, visualizar los datos geoespaciales y simular escenarios alternativos para políticas sostenibles.

## Estructura general

- `data/`: contiene datos originales y procesados.
- `notebooks/`: contiene análisis en Jupyter.
- `src/`: código fuente del proyecto dividido por funciones.
- `app/`: app visual (ej. Streamlit o Dash).
- `docs/`: documentación técnica y científica.
- `tests/`: pruebas automáticas y validaciones.

## Tecnologías
Python, pandas, geopandas, folium, dash/streamlit, mesa, docker
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_general)

# requirements.txt
requirements_content = """pandas
geopy
geopandas
folium
plotly
dash
streamlit
mesa
"""

with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write(requirements_content)

print("Estructura del proyecto y README.md generados correctamente.")


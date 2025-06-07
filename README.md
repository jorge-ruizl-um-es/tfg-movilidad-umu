# Proyecto: Análisis de movilidad laboral y huella de carbono

Este proyecto tiene como objetivo analizar los desplazamientos laborales de una organización, calcular su huella de carbono, visualizar los datos geoespaciales y simular escenarios alternativos para políticas sostenibles.


## ────────────── 📁 ESTRUCTURA DE CARPETAS ──────────────

```
 raiz_del_proyecto/
 ├── data/                  # Datos originales y procesados
 │   ├── raw/              # Excel original
 │   ├── processed/        # CSV/GeoJSON enriquecido
 ├── notebooks/            # Cuadernos Jupyter de análisis
 ├── src/                  # Código fuente del proyecto
 │   ├── geo/              # Georreferenciación, distancias
 │   ├── emissions/        # Cálculo de huella de carbono
 │   ├── visualization/    # Mapas, dashboards
 │   ├── simulation/       # Simulador de trayectos
 │   └── utils.py          # Funciones auxiliares
 ├── app/                  # App Streamlit o Dash (opcional)
 │   └── main.py           # Interfaz de usuario para explorar y simular escenarios
 ├── docs/                 # Documentación técnica y científica
 ├── tests/                # Pruebas automáticas
 ├── requirements.txt      # Dependencias
 ├── docker-compose.yml    # Infraestructura reproducible
 ├── Dockerfile            # Imagen para ejecutar la app en Streamlit
 ├── README.md             # Descripción general del proyecto
```

- `data/`: contiene datos originales y procesados.
- `notebooks/`: contiene análisis en Jupyter.
- `src/`: código fuente del proyecto dividido por funciones.
- `app/`: app visual (ej. Streamlit o Dash).
- `docs/`: documentación técnica y científica.
- `tests/`: pruebas automáticas y validaciones.

## Módulos del proyecto
- Limpieza y enriquecimiento de datos
- Geocodificación de residencias y trabajos
- Cálculo de distancias y modos de transporte
- Estimación de emisiones de CO2
- Visualización de trayectos sobre mapas
- Simulación basada en agentes
- Generación de informes y recomendaciones

## Tecnologías
Python, pandas, geopandas, folium, dash/streamlit, mesa, docker

## Organización
Este repositorio está pensado para dar soporte a varios TFGs conectados entre sí, que pueden trabajar de forma modular.

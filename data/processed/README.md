# data/processed

Datos transformados y enriquecidos (ej. CSV con coordenadas, GeoJSON, etc.).

Datos enriquecidos con:

* Coordenadas geográficas de residencia y lugar de trabajo (latitud y longitud).
* Cálculo de la distancia en kilómetros entre ambos puntos usando la fórmula de Haversine.

Esto proporciona la base para:

* **Estimar el modo de transporte más probable.**
* **Calcular las emisiones diarias/anuales de CO₂ por persona.**
* **Visualizar sobre un mapa los desplazamientos reales.**

Módulos relevantes:

* El módulo `src/emissions/model.py` con la función `estimate_emissions`.
* El módulo `src/geo/distance.py` con la función `haversine_km`.
* La ampliación del cuaderno `analisis_inicial.ipynb` para incluir estimación de modo de transporte y cálculo de emisiones.
* Pruebas automáticas para ambos módulos (`test_emissions.py` y `test_geo.py`).



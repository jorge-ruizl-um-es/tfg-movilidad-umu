# 🔧 Proyecto Global: “Análisis y simulación del impacto medioambiental de los desplazamientos laborales”

Este conjunto de datos ofrece un punto de partida excelente para un proyecto interdisciplinar de análisis de datos, desarrollo de software y visualización geoespacial. A continuación te propongo una estructura de proyecto que puede escalarse en varios Trabajos Fin de Grado (TFG), cada uno con un enfoque distinto pero interrelacionado:

---

## 1. **Limpieza y enriquecimiento del dataset**

**Objetivo**: Validar, corregir y completar los datos disponibles.

* **Subproyectos**:

  * Normalización de datos de direcciones (geocodificación inversa).
  * Enriquecimiento con coordenadas GPS (Google Maps API, Nominatim, etc.).
  * Estimación de modos de transporte por distancia/residencia.
  * Inferencia de hábitos de desplazamiento (individual vs compartido, transporte público, etc.).

📘 **TFG orientado a ingeniería de datos / preprocesamiento geoespacial.**

---

## 2. **Cálculo de huella de carbono**

**Objetivo**: Estimar el impacto ambiental derivado del transporte laboral.

* **Subproyectos**:

  * Modelo de cálculo de emisiones (basado en distancia, modo de transporte, tipo de vehículo).
  * Escenarios alternativos (teletrabajo, transporte público, coche compartido).
  * Comparativa de políticas de movilidad.

📘 **TFG de análisis cuantitativo / sostenibilidad / estadística aplicada.**

---

## 3. **Visualización interactiva sobre mapa**

**Objetivo**: Representar gráficamente residencias, desplazamientos y emisiones.

* **Tecnologías posibles**:

  * Folium, Leaflet.js, Kepler.gl o Mapbox para visualización.
  * Dash o Streamlit para interfaz de usuario interactiva.
  * Capas por años o escenarios.

📘 **TFG orientado a visualización y diseño de herramientas interactivas.**

---

## 4. **Simulación de movilidad**

**Objetivo**: Modelar los flujos diarios y analizar el impacto en tráfico/emisiones.

* **Ideas**:

  * Simulación basada en agentes (por ejemplo, con `Mesa`, una librería en Python).
  * Generación de animaciones de trayectos diarios.
  * Estudio de cuellos de botella y eficiencia.

📘 **TFG de ciencia de datos aplicada / modelado / IA.**

---

## 5. **Sistema de soporte a decisiones para políticas de movilidad**

**Objetivo**: Crear una herramienta que permita simular y evaluar el impacto de decisiones.

* **Ejemplos**:

  * Introducción del teletrabajo parcial.
  * Incentivos a transporte público.
  * Cambios en horarios escalonados.

📘 **TFG con enfoque en desarrollo web/backend + optimización.**

---

## 6. **Análisis temporal y sociodemográfico**

**Objetivo**: Explorar la evolución histórica de patrones de residencia y movilidad.

* **Enfoques posibles**:

  * Series temporales.
  * Cambios en patrones laborales (pre/post pandemia, etc.).
  * Análisis geodemográfico (agrupación de zonas).

📘 **TFG de análisis exploratorio y minería de datos temporal-espacial.**

---

## 7. **Infraestructura y publicación del proyecto**

**Objetivo**: Diseñar una plataforma abierta y reproducible.

* Documentación del dataset (diccionario de datos, esquema).
* Contenedores Docker para reproducibilidad.
* Repositorio y demo pública.

📘 **TFG orientado a ingeniería del software, DevOps y buenas prácticas.**

---

### 🔄 **Enfoque colaborativo**

Puedes diseñar el proyecto como un repositorio común donde cada alumno trabaje en una parte modular (con issues, milestones, etc.), fomentando la colaboración y prácticas reales de trabajo en equipo de ciencia de datos.


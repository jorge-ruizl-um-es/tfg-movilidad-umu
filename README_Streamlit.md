# 🌍 Simulación de Huella de Carbono Laboral

Este repositorio contiene una aplicación interactiva construida con **Streamlit** que permite visualizar y simular el impacto de los desplazamientos laborales sobre la huella de carbono.

## 🧭 ¿Qué hace esta app?

- Visualiza datos reales o simulados sobre trayectos diarios al trabajo.
- Estima las emisiones de CO₂ por persona y modo de transporte.
- Permite simular escenarios alternativos, como que un % de personas usen transporte público.
- Muestra el ahorro total de CO₂ en distintos escenarios.

---

## 🚀 Despliegue en Streamlit Cloud


Puedes desplegar esta app gratuitamente en [Streamlit Community Cloud](https://streamlit.io/cloud). Sigue estos pasos:

### 1. Crea el repositorio en GitHub

Incluye los siguientes archivos y carpetas:

```

.
├── app/
│   └── main.py                # Punto de entrada de la app
├── src/                       # Módulos de cálculo (emisiones, distancia, etc.)
├── data/processed/
│   └── datos\_movilidad\_coordenadas.csv  # Datos de entrada (debe ser público o anonimizado)
├── requirements.txt
├── README.md

```

> ⚠️ Asegúrate de **anonimizar** los datos si contienen información sensible.

### 2. Configura el archivo `requirements.txt`

Ejemplo básico:

```

streamlit
pandas
numpy

```

Añade cualquier otra librería que uses como `matplotlib`, `seaborn`, etc.

### 3. Despliega en Streamlit Cloud

- Inicia sesión en: [https://streamlit.io/cloud](https://streamlit.io/cloud)
- Pulsa en **“New app”**
- Elige tu repositorio
- Establece como archivo principal: `app/main.py`
- Haz clic en **Deploy**

Tu app estará disponible en una URL pública como:

```
https\://<tu-usuario>.streamlit.app/movilidad-laboral
```

---

## 🧪 Ejecución local (opcional)

```bash
# Instala las dependencias
pip install -r requirements.txt

# Lanza la app
streamlit run app/main.py
````

O usa Docker:

```bash
docker compose up --build
```

---

## 📄 Licencia

Este proyecto puede utilizarse como base educativa para TFGs o investigación en sostenibilidad, movilidad y ciencia de datos.


---

¿Quieres que este README se añada también como sección final al documento que estás editando en canvas, o lo prefieres como un archivo separado?
```

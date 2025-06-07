# Imagen base oficial de Python con soporte para Streamlit
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Puerto que expone Streamlit por defecto
EXPOSE 8501

# Comando para lanzar la app
CMD ["streamlit", "run", "app/main.py"]
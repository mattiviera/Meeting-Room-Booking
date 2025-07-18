# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos a la imagen
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que corre Flask
EXPOSE 5000

# Ejecuta la app
CMD ["python", "src/main.py"]

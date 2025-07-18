FROM python:3.11-slim

WORKDIR /app

# Copia todo el proyecto
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Establece el directorio de trabajo dentro de src
WORKDIR /app/src

# Expone el puerto
EXPOSE 5000

# Ejecuta la app Flask
CMD ["python", "-m", "src.main"]



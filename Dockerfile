# Usa imagen oficial Python
FROM python:3.11-slim

# Establece directorio de trabajo
WORKDIR /app

# Copia archivos de requerimientos e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código fuente
COPY ./src ./src

# Expone el puerto en el que Flask correrá
EXPOSE 5000

# Define variable de entorno para que Flask detecte la app
ENV FLASK_APP=src.main
ENV FLASK_ENV=development

# Comando para correr la app
CMD ["flask", "run", "--host=0.0.0.0"]

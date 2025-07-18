# 📅 Sistema de Reservas de Salas

Aplicación web simple para gestionar usuarios, salas y reservas de reuniones.

## 🚀 Funcionalidades

- Crear, editar y eliminar usuarios
- Crear, editar y eliminar salas de reunión
- Crear reservas entre usuarios y salas
- Filtrar reservas por usuario o sala
- UI responsiva y moderna

## 🧱 Tecnologías

- Python 3
- Flask
- Jinja2
- HTML/CSS (estilizado propio)
- Estructura en memoria (no requiere base de datos)

## 📦 Instalación

1. Cloná el repositorio:

   ```bash
   git clone https://github.com/mattiviera/Meeting-Room-Booking.git
   cd meeting-room-booking
   ```

Creá y activá un entorno virtual:

python -m venv venv
source venv/bin/activate # En Linux/macOS
venv\Scripts\activate # En Windows

Instalá las dependencias:

pip install -r requirements.txt

Ejecutá la app:
python src/main.py

Abrí en tu navegador:
http://localhost:5000

## Uso con Docker

### Construir la imagen Docker

Desde la raíz del proyecto (donde está el `Dockerfile`), ejecuta:

docker build -t meeting-room-app .

Esto crea una imagen llamada `meeting-room-app` con todo lo necesario para correr la aplicación.

---

### Ejecutar el contenedor

Para levantar la app en un contenedor y mapear el puerto 5000 al host, ejecuta:

docker run -p 5000:5000 meeting-room-app

---

### Acceder a la aplicación

Abre tu navegador y entra a:

http://localhost:5000/

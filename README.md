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
   git clone https://github.com/tu-usuario/meeting-room-booking.git
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

🗂 Estructura del Proyecto

meeting-room-booking/
├── src/
│ ├── main.py
│ ├── models/
│ ├── repositories/
│ ├── templates/
│ └── static/
│ └── style.css
├── requirements.txt
└── README.md

# Proyecto de carga y filtrado de clientes

Este proyecto utiliza Docker para levantar un entorno con PostgreSQL y ejecutar un script en Python que carga datos desde un archivo CSV, los guarda en la base de datos, realiza filtros y genera un nuevo CSV.

Estructura del proyecto:

mi_proyecto/
├── app/
│   ├── prueba.py
│   ├── data/
│   │   ├── clientes.csv
│   │   └── clientes_filtrados.csv
├── .env
├── docker-compose.yml
├── requirements.txt
└── README.md

Requisitos: Docker y Docker Compose.

Instrucciones de ejecución:

1. Clonar el repositorio:
git clone 
cd mi_proyecto

2. Crear el archivo .env basado en .env.example

3. Construir y levantar los contenedores:
docker compose up -d --build

4. Ejecutar el script:
docker compose exec app python /app/prueba.py

5. El archivo de salida se generará en:
app/data/clientes_filtrados.csv

Tecnologías utilizadas: Python, pandas, SQLAlchemy, PostgreSQL, Docker

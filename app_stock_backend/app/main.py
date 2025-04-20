from app.api.api_main import app





# models/	Define las tablas de tu base de datos (SQLAlchemy)
# schemas/	Define los esquemas de entrada/salida (usando Pydantic)
# crud/	Contiene la lógica de acceso a datos, o sea: lectura, escritura, actualización, eliminación
# routes/	Define las rutas (endpoints) que van a consumir tus clientes
# api/api_main.py	Crea la instancia FastAPI() y conecta los routers
# main.py	Solo importa la app y sirve como punto de entrada
# database.py	Configura la conexión a la base de datos
# config.py	Lee las variables del .env


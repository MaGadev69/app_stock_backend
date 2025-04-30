from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import productos  # cuando agreguemos más routers, los importás acá
# CONSTRUCTOR PRINCIPAL
app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes, puedes especificar los dominios específicos si lo deseas
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP, como GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(productos.router, prefix="/productos", tags=["productos"])
# quiero que todo lo que esté en el router productos esté disponible bajo la URL /productos



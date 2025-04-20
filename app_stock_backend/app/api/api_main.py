from fastapi import FastAPI
from app.routes import productos  # cuando agreguemos más routers, los importás acá
# CONSTRUCTOR PRINCIPAL
app = FastAPI()

app.include_router(productos.router, prefix="/productos", tags=["productos"])
# quiero que todo lo que esté en el router productos esté disponible bajo la URL /productos



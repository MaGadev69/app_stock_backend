from fastapi import FastAPI
from app.routes import productos  # cuando agreguemos más routers, los importás acá

app = FastAPI()

app.include_router(productos.router, prefix="/productos", tags=["productos"])

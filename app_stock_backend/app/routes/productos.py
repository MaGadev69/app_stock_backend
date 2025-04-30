from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.productos import ProductoRead
from app.database import get_db
from app.crud.productos import get_productos, contar_productos_activos

router = APIRouter()

@router.get("/", response_model=list[ProductoRead])
def listar_productos(db: Session = Depends(get_db)):
    return get_productos(db)
@router.get("/productos/activos/cantidad")
def obtener_cantidad_productos_activos(db: Session = Depends(get_db)):
    return {"cantidad": contar_productos_activos(db)}
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.productos import get_productos
from app.schemas.productos import ProductoRead
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[ProductoRead])
def listar_productos(db: Session = Depends(get_db)):
    return get_productos(db)

from pydantic import BaseModel
from datetime import datetime

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    id_proveedor: int
    stock: int
    imagen = str
    categoria = str
    estado = str
    fecha_creacion = datetime
    fecha_ultima_modificacion = datetime


class ProductoCreate(ProductoBase):
    pass


class ProductoRead(ProductoBase):
    id_producto: int
    nombre: str
    descripcion: str
    precio: float
    id_proveedor: int
    stock: int
    
    class Config:
        orm_mode = True

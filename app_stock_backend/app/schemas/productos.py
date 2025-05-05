from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    id_proveedor: int
    stock: int
    imagen: str
    categoria: str
    estado: str
    fecha_creacion: datetime
    fecha_ultima_modificacion: datetime

class ProductoCreate(ProductoBase):
    pass

class ProductoRead(ProductoBase):
    id_producto: int

    class Config:
        #orm_mode = True
        #* 'orm_mode' has been renamed to 'from_attributes'
        model_config = ConfigDict(from_attributes=True)

# ProductoBase agrupa todos los campos comunes.

# ProductoCreate lo hereda tal cual (para usar cuando se crea un producto).

# ProductoRead hereda los mismos campos y le agrega solo el id_producto, 
# que generalmente es autogenerado por la base de datos y no se incluye al crear.
from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    precio = Column(Float)
    id_proveedor = Column(Integer)
    stock = Column(Integer)
    imagen = Column(String)
    categoria = Column(String)
    estado = Column(String)
    fecha_creacion = Column(DateTime)
    fecha_ultima_modificacion = Column(DateTime)

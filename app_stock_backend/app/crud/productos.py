from sqlalchemy.orm import Session
from app.models.productos import Producto
from app.schemas.productos import ProductoCreate

# Obtener todos los productos
def get_productos(db: Session):
    return db.query(Producto).all()

# Obtener cantidad de productos activos
def contar_productos_activos(db: Session):
    return db.query(Producto).filter(Producto.estado == "activo").count()

# Obtener un producto por ID
def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id_producto == producto_id).first()

# Crear un nuevo producto
def create_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# Eliminar un producto
def delete_producto(db: Session, producto_id: int):
    producto = db.query(Producto).filter(Producto.id_producto == producto_id).first()
    if producto:
        db.delete(producto)
        db.commit()
        return True
    return False

# Actualizar un producto
def update_producto(db: Session, producto_id: int, datos_actualizados: ProductoCreate):
    producto = db.query(Producto).filter(Producto.id_producto == producto_id).first()
    if producto:
        for key, value in datos_actualizados.dict().items():
            setattr(producto, key, value)
        db.commit()
        db.refresh(producto)
        return producto
    return None

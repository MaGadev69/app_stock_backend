Este proyecto es una API para gestionar productos en un sistema de inventario.

## Requisitos
- Python 3.11
- Docker

## Instalación
1. Clona el repositorio.
2. Crea un archivo `.env` con las variables de entorno.
3. Construye y ejecuta los contenedores:
   docker-compose up --build

Reglas de negocio del sistema de gestion y logistica.

# Usuarios:
Todo usuario debe pertenecer al menos a una sucursal.
Todos los usuarios tienen roles: admin (puede ver, modificar y gestionar todo) y empleado (acceso limitado a operaciones como generación de remitos).
Todos los usuarios deben iniciar sesión con credenciales válidas.
Los admin pueden crear, modificar o desactivar otros usuarios.
# Proveedores:
Solo los proveedores activos pueden asociarse a nuevos productos.
Los productos deben estar vinculados a un proveedor existente y activo.
# Productos:
Cada producto debe tener un nombre único por proveedor, categoría, precio y stock inicial.
El stock de un producto se mantiene de forma separada por cada sucursal.
Los productos no pueden ser trasladados si el stock disponible en la sucursal origen es insuficiente.
Los productos inactivos no pueden incluirse en nuevos remitos.

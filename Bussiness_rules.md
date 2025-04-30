# Business Rules

## Usuarios
- Todo usuario debe pertenecer a una única sucursal, los administradores pueden no estar asignados a una sucursal.
- **Roles de usuarios**:
  - `admin`: Todos los permisos.
  - `empleado`: 
    - Crear remitos.
    - Visualizar productos.
    - Cargar stock (solo en su sucursal).
- **Autenticación**: Los usuarios deben iniciar sesión con credenciales válidas.
- **Estado**: El usuario debe estar activo para operar.
- **Administradores**: Pueden crear, modificar o desactivar otros usuarios.

## Proveedores
- **Datos obligatorios**: Nombre, estado (`activo`/`inactivo`) y datos de contacto.
- **Restricciones**:
  - Solo proveedores activos pueden asociarse a nuevos productos.
  - Eliminar un proveedor solo es posible si no tiene productos asociados activos.
- **Productos**: Deben estar vinculados a un proveedor existente y activo.

## Productos
- **Atributos obligatorios**:
  - Nombre único.
  - Proveedor activo asociado.
  - Estado activo para ser transferible o visible.
  - Precio mayor a 0.
- **Reglas**:
  - `id_proveedor` debe existir y estar activo.
  - Modificables: nombre, descripción, precio, `id_proveedor`.
  - No se puede eliminar un producto con stock en alguna sucursal (solo marcar como inactivo).
  - Stock separado por sucursal.
  - Productos inactivos no pueden incluirse en nuevos remitos.
- **Historial**: Cada modificación (precio, proveedor, estado, categoría) se registra en `historial_cambios`.

## Sucursales
- **Casa Central**:
  - Reglas diferenciadas.
  - Receptora de formularios de pedidos.
  - Stock maestro.
- **General**:
  - Nombre único.
  - Solo sucursales activas pueden operar movimientos de stock o tener empleados asignados.
  - Sucursal inactiva no puede ser origen/destino en remitos.

## Remitos
- **Datos obligatorios**:
  - Sucursal origen, sucursal destino, usuario responsable, fecha y estado.
- **Reglas**:
  - No puede generarse un remito entre la misma sucursal (origen = destino).
  - Solo un administrador puede modificar el estado del remito.
  - Productos deben tener cantidad y precio unitario definidos.
  - Validar que `remitosproductos.cantidad` no supere el stock de la sucursal origen.
- **Proceso de recepción**:
  - Se descuenta stock de la sucursal origen.
  - Se incrementa stock en la sucursal destino (al verificar).
  - Remito anulado no afecta stock de Casa Central.
- **Validaciones**:
  - `id_empleado` debe pertenecer a `id_sucursal_origen`.
  - Estados posibles: `pendiente`, `en tránsito`, `recibido`, `anulado`.
  - Solo un admin puede anular un remito en estado `pendiente`.
  - No pueden haber productos duplicados en un mismo remito.
  - La cantidad debe ser mayor a cero.

---

# Módulo de Pedidos

## Creación de Pedidos
- Solo puede ser generado por una sucursal distinta a Casa Central.
- Estado inicial: `pendiente`.

## Estados de Pedido
Posibles: `pendiente`, `aprobado`, `rechazado`, `enviado`, `completo`.
- Solo un administrador puede cambiar el estado.

## Validaciones
- No se puede crear un pedido sin al menos un producto en `pedido_detalle`.
- Casa Central puede tener múltiples pedidos `pendiente` activos.
- **Observaciones**: Comentarios opcionales para detalles/urgencias.

## Productos en el Pedido
- Solo productos existentes en la tabla `productos`.
- Cantidad solicitada > 0.
- **Restricción**: No se puede agregar el mismo producto más de una vez en un pedido.
- **Relación**: Cada línea de detalle está asociada a un solo `id_pedido`.

## Procesamiento del Pedido
- **Aprobado**:
  - Casa Central genera transferencia de stock hacia la sucursal solicitante.
  - Se genera automáticamente un remito relacionado.
- **Completado**:
  - Verificar que todos los productos fueron transferidos y recibidos.
  - Solo se marca como `completo` si toda la mercadería fue entregada.

---

# Historial de Cambios
Registra cambios relevantes en `historial_cambios` para auditoría y trazabilidad.

## Cambios Registrados
- Creaciones, modificaciones y eliminaciones de entidades clave.
- Cambios de estado (pedidos, remitos, etc.).
- Modificaciones en campos importantes (precios, stock, etc.).

## Estructura del Log
- `id_cambio`: Identificador único.
- `tipo`: Acción (`creacion`, `modificacion`, `eliminacion`, `estado`).
- `entidad_afectada`: Tabla/módulo afectado.
- `id_entidad`: ID del registro.
- `campo`: Campo modificado (si aplica).
- `valor_anterior` y `valor_nuevo`.
- `fecha`: Fecha y hora del cambio.
- `id_usuario`: Usuario que realizó la acción.

**Ejemplo** (para creación de pedido):
```sql
tipo = 'creacion',
entidad = 'pedidos',
id_entidad = id_pedido,
campo = 'estado',
valor_anterior = NULL,
valor_nuevo = 'pendiente',
fecha = 'fecha',
id_usuario = 'usuario'

---

## Flujo Normal - Factura Electrónica

[Venta en el Sistema] 
      ↓
[Generar Comprobante]
      ↓
[Enviar a AFIP WebService]
      ↓
[AFIP responde OK → CAE recibido]
      ↓
[Factura Electrónica emitida]
      ↓
[Entrega al cliente (PDF/impresión)]

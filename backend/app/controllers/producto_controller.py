from app.models import db
from app.models.producto import Producto


class ProductoController:

    @staticmethod
    def get_all():
        productos = Producto.query.all()

        return [
            {
                "id": p.id,
                "nombre": p.nombre,
                "descripcion": p.descripcion,
                "precio_costo": float(p.precio_costo),
                "precio_venta": float(p.precio_venta),
                "stock_actual": p.stock_actual,
                "stock_minimo": p.stock_minimo,
                "categoria_id": p.categoria_id,
                "proveedor_id": p.proveedor_id
            }
            for p in productos
        ], 200


    @staticmethod
    def show(id):
        producto = Producto.query.get(id)

        if not producto:
            return {"message": "Producto no encontrado"}, 404

        return {
            "id": producto.id,
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "precio_costo": float(producto.precio_costo),
            "precio_venta": float(producto.precio_venta),
            "stock_actual": producto.stock_actual,
            "stock_minimo": producto.stock_minimo,
            "categoria_id": producto.categoria_id,
            "proveedor_id": producto.proveedor_id
        }, 200


    @staticmethod
    def create(data):
        try:
            nuevo = Producto(
                nombre=data["nombre"],
                descripcion=data.get("descripcion"),
                precio_costo=data["precio_costo"],
                precio_venta=data["precio_venta"],
                stock_actual=data.get("stock_actual", 0),
                stock_minimo=data.get("stock_minimo", 0),
                categoria_id=data["categoria_id"],
                proveedor_id=data.get("proveedor_id")
            )

            db.session.add(nuevo)
            db.session.commit()

            return {
                "message": "Producto creado correctamente",
                "id": nuevo.id
            }, 201

        except Exception as e:
            db.session.rollback()
            return {"message": "Error al crear producto", "error": str(e)}, 500


    @staticmethod
    def update(data, id):
        producto = Producto.query.get(id)

        if not producto:
            return {"message": "Producto no encontrado"}, 404

        try:
            producto.nombre = data.get("nombre", producto.nombre)
            producto.descripcion = data.get("descripcion", producto.descripcion)
            producto.precio_costo = data.get("precio_costo", producto.precio_costo)
            producto.precio_venta = data.get("precio_venta", producto.precio_venta)
            producto.stock_actual = data.get("stock_actual", producto.stock_actual)
            producto.stock_minimo = data.get("stock_minimo", producto.stock_minimo)
            producto.categoria_id = data.get("categoria_id", producto.categoria_id)
            producto.proveedor_id = data.get("proveedor_id", producto.proveedor_id)

            db.session.commit()

            return {"message": "Producto actualizado correctamente"}, 200

        except Exception as e:
            db.session.rollback()
            return {"message": "Error al actualizar producto", "error": str(e)}, 500


    @staticmethod
    def destroy(id):
        producto = Producto.query.get(id)

        if not producto:
            return {"message": "Producto no encontrado"}, 404

        try:
            db.session.delete(producto)
            db.session.commit()

            return {"message": "Producto eliminado correctamente"}, 200

        except Exception as e:
            db.session.rollback()
            return {"message": "Error al eliminar producto", "error": str(e)}, 500
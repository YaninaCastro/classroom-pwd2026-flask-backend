from flask import Response, jsonify, request
from app.database import db

from app.models.movimiento_stock import MovimientoStock               #Accedo a los atributos de MovimientoStock
from app.models.producto import Producto

from flask_jwt_extended import get_jwt_identity
from app.controllers import Controller                                


class MovimientoStockController(Controller):

    @staticmethod
    def get_all() -> tuple[Response, int]:
        movimientos = db.session.execute(
            db.select(MovimientoStock).order_by(db.desc(MovimientoStock.id))
        ).scalars().all()

        if len(movimientos) > 0:
            return jsonify([m.to_dict() for m in movimientos]), 200

        return jsonify({"error": "datos no encontrados"}), 404


    @staticmethod
    def mis_movimientos() -> tuple[Response, int]:
        user_id = get_jwt_identity()

        movimientos = db.session.execute(
            db.select(MovimientoStock)
            .where(MovimientoStock.user_id == user_id)
            .order_by(db.desc(MovimientoStock.id))
        ).scalars().all()

        if len(movimientos) > 0:
            return jsonify([m.to_dict() for m in movimientos]), 200

        return jsonify({"error": "datos no encontrados"}), 404


    @staticmethod
    def create(request) -> tuple[Response, int]:
        tipo: str = request.get("tipo")
        cantidad: int = request.get("cantidad")
        producto_id: int = request.get("producto_id")
        motivo: str = request.get("motivo")

        # Validaciones básicas
        if tipo not in ["entrada", "salida"]:
            return jsonify({"error": "Tipo inválido"}), 422

        if not cantidad or cantidad <= 0:
            return jsonify({"error": "La cantidad debe ser mayor a 0"}), 422

        if not producto_id:
            return jsonify({"error": "producto_id es requerido"}), 422

        # Busca el producto
        producto = db.session.get(Producto, producto_id)

        if not producto:
            return jsonify({"error": "producto no encontrado"}), 404

        # Lógica del stock
        if tipo == "salida":
            if producto.stock_actual < cantidad:
                return jsonify({"error": "Stock insuficiente para registrar la salida"}), 400

            producto.stock_actual -= cantidad

        else:  # entrada
            producto.stock_actual += cantidad
            
        db.session.add(producto)
        # User desde JWT
        user_id = int(get_jwt_identity())

        # Crear el movimiento
        movimiento = MovimientoStock(
            tipo=tipo,
            cantidad=cantidad,
            motivo=motivo,
            producto_id=producto_id,
            user_id=user_id
        )

        db.session.add(movimiento)
        db.session.commit()

        return jsonify({"message": "movimiento registrado con exito"}), 201
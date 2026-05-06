from sqlalchemy.exc import IntegrityError
from flask import Response, jsonify, request

from app.models.categoria import Categoria    #Accedo a los atributos de Categoría
from app.database import db
from app.controllers import Controller        #Utilizo los métodos de la interfaz


class CategoriaController(Controller):

    @staticmethod
    def get_all() -> tuple[Response, int]:
        categorias_list = db.session.execute(
            db.select(Categoria).order_by(db.desc(Categoria.id))
        ).scalars().all()

        if len(categorias_list) > 0:
            categorias_dict = [c.to_dict() for c in categorias_list]
            return jsonify(categorias_dict), 200

        return jsonify({"message": "datos no encontrados"}), 404


    @staticmethod
    def show(id) -> tuple[Response, int]:
        categoria = db.session.get(Categoria, id)

        if categoria:
            return jsonify(categoria.to_dict()), 200

        return jsonify({"message": "categoria no encontrada"}), 404


    @staticmethod
    def create(request) -> tuple[Response, int]:
        nombre: str = request.get("nombre")
        descripcion: str = request.get("descripcion")

        if not nombre:
            return jsonify({"message": "El nombre es requerido"}), 422

        try:
            categoria = Categoria(
                nombre=nombre,
                descripcion=descripcion
            )

            db.session.add(categoria)
            db.session.commit()

            return jsonify({"message": "categoria creada con exito"}), 201

        except IntegrityError:
            db.session.rollback()
            return jsonify({"message": "categoria ya registrada"}), 409


    @staticmethod
    def update(request, id) -> tuple[Response, int]:
        categoria = db.session.get(Categoria, id)

        if not categoria:
            return jsonify({"message": "categoria no encontrada"}), 404

        nombre: str = request.get("nombre")
        descripcion: str = request.get("descripcion")

        if not nombre:
            return jsonify({"message": "El nombre es requerido"}), 422

        try:
            categoria.nombre = nombre
            categoria.descripcion = descripcion

            db.session.commit()

            return jsonify({"message": "categoria modificada con exito"}), 200

        except IntegrityError:
            db.session.rollback()
            return jsonify({"message": "el nombre ya existe"}), 409


    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        categoria = db.session.get(Categoria, id)

        if not categoria:
            return jsonify({"message": "categoria no encontrada"}), 404

        db.session.delete(categoria)
        db.session.commit()

        return jsonify({"message": "categoria eliminada con exito"}), 200
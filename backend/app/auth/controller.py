from app.database import db
from app.models.user import User
from app.models.rol import Rol
from flask import Response, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity
from sqlalchemy.exc import IntegrityError


class AuthController:

    @staticmethod
    def register(request: dict) -> tuple[Response, int]:
        nombre = request.get('nombre')
        email = request.get('email')
        password = request.get('password')

        if not nombre or not email or not password:
            return jsonify({'message': 'Faltan datos'}), 422

        try:
            # operador
            rol_user = db.session.execute(
                db.select(Rol).filter_by(nombre='operador')
            ).scalar_one_or_none()

            if not rol_user:
                return jsonify({'message': 'Rol operador no existe'}), 500

            user = User(
                nombre=nombre,
                email=email,
                rol_id=rol_user.id
            )

            user.generate_password(password)

            db.session.add(user)
            db.session.commit()

            return jsonify({'message': "usuario creado con exito"}), 201

        except IntegrityError:
            db.session.rollback()
            return jsonify({'message': "Usuario ya registrado"}), 409

    @staticmethod
    def login(request: dict) -> tuple[Response, int]:
        email = request.get('email')
        password = request.get('password')

        if not email or not password:
            return jsonify({'message': 'Faltan datos'}), 422

        user = db.session.execute(
            db.select(User).filter_by(email=email)
        ).scalar_one_or_none()

        if user and user.validate_password(password):
            access_token = create_access_token(
                identity=str(user.id),
                additional_claims={
                    'rol': user.rol.nombre if user.rol else None
                }
            )

            return jsonify({
                'access_token': access_token,
                'rol': user.rol.nombre if user.rol else None,
                'nombre': user.nombre
            }), 200

        return jsonify({'message': "Credenciales inválidas"}), 401

    @staticmethod
    def me() -> tuple[Response, int]:
        user_id = get_jwt_identity()

        user = db.session.get(User, user_id)

        if not user:
            return jsonify({'message': 'Usuario no encontrado'}), 404

        return jsonify({
            'id': user.id,
            'nombre': user.nombre,
            'email': user.email,
            'rol': user.rol.nombre if user.rol else None
        }), 200

from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.auth.controller import AuthController

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.post('/register')
def register():
    return AuthController.register(request.get_json())


@auth_bp.post('/login')
def login():
    return AuthController.login(request.get_json())


@auth_bp.get('/me')
@jwt_required()
def me():
    return AuthController.me()
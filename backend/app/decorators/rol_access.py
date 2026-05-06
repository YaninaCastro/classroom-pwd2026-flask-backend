'''
from functools import wraps
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from app.database import db
from app.models.user import User
from flask import jsonify


def rol_access(*roles_permitidos):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            # 🔒 verifica que haya token válido
            verify_jwt_in_request()

            user_id = get_jwt_identity()

            user = db.session.execute(
                db.select(User).filter_by(id=user_id)
            ).scalar_one_or_none()

            if user and user.rol and user.rol.nombre in roles_permitidos:
                return func(*args, **kwargs)

            return jsonify({
                'message': 'Acceso denegado: rol no autorizado'
            }), 403

        return wrapper
    return decorator
'''

from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt

def rol_access(*roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # verifica que tenga el token en el request, el get_jwt toma los datos del mismo 
            # busca que tenga el claim "rol" 
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("rol") not in roles:
                return jsonify(
                    msg=f"Acceso denegado: se requiere rol {' o '.join(roles)}"
                ), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
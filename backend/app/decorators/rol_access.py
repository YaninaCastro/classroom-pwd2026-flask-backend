
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

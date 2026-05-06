from sqlalchemy.exc import IntegrityError
from app.models.rol import Rol
from app.database import db
from flask import Response, jsonify
from app.controllers import Controller

class RolController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        roles_list = db.session.execute(db.select(Rol).order_by(db.desc(Rol.id))).scalars().all()
        if len( roles_list) >0:
            roles_to_dict = [role.to_dict() for role in roles_list ]
            return jsonify(roles_to_dict), 200 
        return jsonify({"message": 'datos no encontrados'}), 404
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        role = db.session.get(Rol, id)
        if role:
            return jsonify(role.to_dict()), 200
        return jsonify({"message": 'rol no encontrado'}), 404
    
    @staticmethod
    def create(request) -> tuple[Response, int]:
        nombre:str = request['nombre']
        
        error :str | None = None
        if nombre is None:
            error = 'El nombre es requerido'
            
        if error is None:
            try:
                rol = Rol(nombre=nombre)
                db.session.add(rol)
                db.session.commit()
                return jsonify({'message': "rol creado con exito"}), 201
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': "rol ya registrado"}), 409
        return jsonify ({'message': error}), 422
        
        
    @staticmethod
    def update(request, id)->tuple[Response, int]:
        nombre:str = request['nombre']
        error :str | None = None
        if nombre is None:
            error = 'El nombre es requerido'
            
        if error is None:
            role = db.session.get(Rol, id)
            if role:
                try:
                    role.nombre = nombre
                    db.session.commit()
                    return jsonify({'message':'rol modificado con exito'}), 200
                except IntegrityError:
                    error = 'el nombre ya existen' 
                    return jsonify({'message':error}), 409
            else:     
                error = 'role no encontrado'
            
        return jsonify({'message':error}), 404
        
    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        rol = db.session.get(Rol, id)
        error = None
        if rol:
            db.session.delete(rol)
            db.session.commit()
            return jsonify({'message':'el rol fue eliminado con exito'}), 200
        else:
            error = 'rol no encontrado'
        return jsonify({'message':error}), 404
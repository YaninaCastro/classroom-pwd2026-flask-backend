from app.models.proveedor import Proveedor
from app.database import db

class ProveedorController:

    @staticmethod
    def get_all():
        return Proveedor.query.all()

    @staticmethod
    def get_by_id(id):
        return Proveedor.query.get(id)

    @staticmethod
    def create(data):
        nuevo = Proveedor(
            nombre=data.get("nombre"),
            contacto=data.get("contacto"),
            telefono=data.get("telefono"),
            email=data.get("email")
        )
        db.session.add(nuevo)
        db.session.commit()
        return nuevo
    
    @staticmethod
    def delete(prov):
        db.session.delete(prov)
        db.session.commit()
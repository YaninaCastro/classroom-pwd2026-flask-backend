from app.database import db
from app.models.base_model import BaseModel


class Proveedor(BaseModel):
    __tablename__ = "proveedores"

    nombre = db.Column(db.String(150), nullable=False)
    contacto = db.Column(db.String(100))
    telefono = db.Column(db.String(30))
    email = db.Column(db.String(120))
    
    
    def to_dic(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "contacto": self.contacto,
            "telefono": self.telefono,
            "email": self.email
        }
        
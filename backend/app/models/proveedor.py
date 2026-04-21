from app.models import db
from app.models.base_model import BaseModel


class Proveedor(BaseModel):
    __tablename__ = "proveedores"

    nombre = db.Column(db.String(150), nullable=False)
    contacto = db.Column(db.String(100))
    telefono = db.Column(db.String(30))
    email = db.Column(db.String(120))
    
    
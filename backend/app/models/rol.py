from app.database import db
from app.models.base_model import BaseModel

class Rol(BaseModel):
    __tablename__="roles"
    nombre = db.Column(db.String, unique = True)
    activo = db.Column(db.String(1), default = 'S')
    
    
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
from app.database import db
from app.models.base_model import BaseModel


class MovimientoStock(BaseModel):
    __tablename__ = 'movimientos_stock'

    tipo = db.Column(db.String(10), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    motivo = db.Column(db.String(200), nullable=True)

    producto_id = db.Column(
        db.Integer,
        db.ForeignKey('productos.id'),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )


    producto = db.relationship('Producto', backref='movimientos')
    user = db.relationship('User', backref='movimientos')

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "cantidad": self.cantidad,
            "motivo": self.motivo,
            "producto": {
                "id": self.producto.id,
                "nombre": self.producto.nombre
            } if self.producto else None,
            "user": {
                "id": self.user.id,
                "nombre": self.user.nombre
            } if self.user else None,
            "created_at": self.created_at
        }


    def __repr__(self):
        return f'<MovimientoStock {self.tipo} - {self.cantidad}>'

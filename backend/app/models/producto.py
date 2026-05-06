from app.database import db
from app.models.base_model import BaseModel

class Producto(BaseModel):
    __tablename__= 'productos'
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio_costo = db.Column(db.Numeric(10,2), nullable=False)
    precio_venta = db.Column(db.Numeric(10,2), nullable=False)
    stock_actual = db.Column(db.Integer, default=0)
    stock_minimo = db.Column(db.Integer, default=0)
    categoria_id = db.Column(db.Integer,db.ForeignKey('categorias.id'),nullable=False)
    proveedor_id = db.Column(db.Integer,db.ForeignKey('proveedores.id'),nullable=True)
    
    categoria = db.relationship('Categoria', backref='productos')
    proveedor = db.relationship('Proveedor', backref='productos')
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio_costo": str(self.precio_costo),
            "precio_venta": str(self.precio_venta),
            "stock_actual": self.stock_actual,
            "stock_minimo": self.stock_minimo,
            "categoria": {
                "id": self.categoria.id,
                "nombre": self.categoria.nombre
            } if self.categoria else None,
            "proveedor": {
                "id": self.proveedor.id,
                "nombre": self.proveedor.nombre
            } if self.proveedor else None
        }
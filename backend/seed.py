'''
from flask_sqlalchemy import SQLAlchemy
from app.models.user import User
from app.models.rol import Rol
from app.database import db
from flask import Flask
from app import create_app

app = create_app()


def seed():
    # Crear roles
    admin_role = Rol(nombre='superadmin')
    user_role = Rol(nombre='user')
    db.session.add_all([admin_role, user_role])
    db.session.commit()

    # Crear usuarios
    admin_user = User(nombre='admin', password='admin123', rol_id=admin_role.id, email='admin@example.com')
    regular_user = User(nombre='user', password='user123', rol_id=user_role.id, email='user@example.com')
    db.session.add_all([admin_user, regular_user])
    db.session.commit()
    
if __name__ == '__main__':
    with app.app_context():
        seed()
'''       
'''     
from app import create_app
from app.database import db
from app.models.rol import Rol
from app.models.user import User
from app.models.categoria import Categoria
from app.models.proveedor import Proveedor
from app.models.producto import Producto

app = create_app()

with app.app_context():
    # Roles
    rol_admin = Rol(nombre='admin')
    rol_op    = Rol(nombre='operador')
    db.session.add_all([rol_admin, rol_op])
    db.session.commit()

    # Usuario admin
    admin = User(username='admin', email='admin@stock.com', rol=rol_admin)
    admin.generate_password('admin123')
    db.session.add(admin)

    # Categorías
    alm = Categoria(nombre='Almacén', descripcion='Productos secos')
    lim = Categoria(nombre='Limpieza', descripcion='Artículos de limpieza')
    db.session.add_all([alm, lim])

    # Proveedor
    prov = Proveedor(nombre='Distribuidora Norte', telefono='2994001234')
    db.session.add(prov)
    db.session.commit()

    # Productos
    db.session.add_all([
        Producto(nombre='Harina 000', precio_costo=280, precio_venta=350,
                 stock_actual=50, stock_minimo=10,
                 categoria_id=alm.id, proveedor_id=prov.id),
        Producto(nombre='Lavandina 1L', precio_costo=150, precio_venta=210,
                 stock_actual=30, stock_minimo=5,
                 categoria_id=lim.id, proveedor_id=prov.id),
    ])
    db.session.commit()
    print("Seed completado.")
'''

from app import create_app
from app.database import db
from app.models.rol import Rol
from app.models.user import User
from app.models.categoria import Categoria
from app.models.proveedor import Proveedor
from app.models.producto import Producto

app = create_app()

with app.app_context():

    # Roles
    rol_admin = Rol(nombre='admin')
    rol_op = Rol(nombre='operador')
    db.session.add_all([rol_admin, rol_op])
    db.session.commit()

    # Usuario admin (CORREGIDO)
    admin = User(
        nombre='admin',
        email='admin@stock.com',
        password='',   # se sobrescribe abajo
        rol_id=rol_admin.id
    )
    admin.generate_password('admin123')
    db.session.add(admin)

    # Categorías
    alm = Categoria(nombre='Almacén', descripcion='Productos secos')
    lim = Categoria(nombre='Limpieza', descripcion='Artículos de limpieza')
    db.session.add_all([alm, lim])
    db.session.commit()

    # Proveedor
    prov = Proveedor(nombre='Distribuidora Norte', telefono='2994001234')
    db.session.add(prov)
    db.session.commit()

    # Productos
    db.session.add_all([
        Producto(
            nombre='Harina 000',
            precio_costo=280,
            precio_venta=350,
            stock_actual=50,
            stock_minimo=10,
            categoria_id=alm.id,
            proveedor_id=prov.id
        ),
        Producto(
            nombre='Lavandina 1L',
            precio_costo=150,
            precio_venta=210,
            stock_actual=30,
            stock_minimo=5,
            categoria_id=lim.id,
            proveedor_id=prov.id
        ),
    ])

    db.session.commit()
    print("Seed completado.")
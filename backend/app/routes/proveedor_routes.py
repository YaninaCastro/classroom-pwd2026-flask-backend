from app.controllers.proveedor_controller import ProveedorController
from flask import Blueprint, request, jsonify

proveedores = Blueprint("proveedores", __name__, url_prefix="/proveedores")

@proveedores.get("/")
def listar():
    data = ProveedorController.get_all()
    return jsonify([{
        "id": p.id,
        "nombre": p.nombre,
        "telefono": p.telefono
    } for p in data])

@proveedores.post("/")
def crear():
    data = request.get_json()
    nuevo = ProveedorController.create(data)

    return jsonify({
        "id": nuevo.id,
        "nombre": nuevo.nombre
    }), 201
    
@proveedores.delete("/<int:id>")
def eliminar(id):
    prov = ProveedorController.get_by_id(id)

    if not prov:
        return {"error": "Proveedor no encontrado"}, 404

    try:
        ProveedorController.delete(prov)
        return {"msg": "Proveedor eliminado"}
    except Exception as e:
        return {"error": str(e)}, 400    

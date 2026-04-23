from app.controllers.producto_controller import ProductoController
from flask import request, Blueprint


productos = Blueprint('productos', __name__, url_prefix='/productos')


@productos.route('/')
def get_all():
    return ProductoController.get_all()


@productos.route('/<int:id>')
def show(id):
    return ProductoController.show(id)


@productos.route("/", methods=['POST'])
def create():
    return ProductoController.create(request.get_json())


@productos.route("/<int:id>", methods=['PUT'])
def update(id):
    return ProductoController.update(
        request=request.get_json(),
        id=id
    )


@productos.route("/<int:id>", methods=['DELETE'])
def destroy(id):
    return ProductoController.destroy(id)

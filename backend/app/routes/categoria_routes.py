from app.controllers.categoria_controller import CategoriaController
from flask import request, Blueprint


categorias = Blueprint('categorias', __name__, url_prefix='/categorias')


@categorias.route('/')
def get_all():
    return CategoriaController.get_all()


@categorias.route('/<int:id>')
def show(id):
    return CategoriaController.show(id)


@categorias.route("/", methods=['POST'])
def create():
    return CategoriaController.create(request.get_json())


@categorias.route("/<int:id>", methods=['PUT'])
def update(id):
    return CategoriaController.update(
        request=request.get_json(),
        id=id
    )


@categorias.route("/<int:id>", methods=['DELETE'])
def destroy(id):
    return CategoriaController.destroy(id)
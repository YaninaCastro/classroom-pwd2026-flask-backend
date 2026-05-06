from app.controllers.movimiento_stock_controller import MovimientoStockController
from flask import request, Blueprint
from app.decorators.rol_access import rol_access

movimientos_stock = Blueprint('movimientos_stock', __name__, url_prefix='/movimientos')


# GET /movimientos/: solo admin
@movimientos_stock.route('/')
@rol_access('admin')                          #Filtro usuario con el decorador de rol: @rol_accss('')
def get_all():
    return MovimientoStockController.get_all()


# GET /movimientos/mis: usuario autenticado (admin u operador)
@movimientos_stock.route('/mis')
@rol_access('admin', 'operador')
def mis_movimientos():
    return MovimientoStockController.mis_movimientos()


# POST /movimientos/: usuario autenticado (admin u operador)
@movimientos_stock.route("/", methods=['POST'])
@rol_access('admin', 'operador')
def create():
    return MovimientoStockController.create(request.get_json())

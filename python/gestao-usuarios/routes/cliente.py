from flask import Blueprint

cliente_route = Blueprint('home', __name__)


@cliente_route.route('/')
def lista_clientes():
    """listar os clientes"""
    pass


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """inserir os dados do cliente"""
    pass


@cliente_route.route('/new')
def form_cliente():
    """formulario para cadastrar um cliente"""
    pass


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """exibir detalhes do cliente"""
    pass


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """formulário para editar um cliente"""
    pass


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """atualizar informções do cliente"""
    pass


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """deletar informções do cliente"""
    pass

from chalice import Blueprint, Response
from chalicelib.controllers.product_controller import (
    list_product, create_product, filter_product_by_id, update_product,
    delete_product
)

product_routes = Blueprint(__name__)

@product_routes.route('/product', methods=['GET'])
def get_all_product():
    get_product, status_code = list_product()
    return Response(
        body=get_product,
        status_code=status_code,
    )


@product_routes.route('/product', methods=['POST'])
def add_product():
    data = product_routes.current_request.json_body
    name = data.get('name')
    price = data.get('price')
    unit_measure_id = data.get('unit_measure_id')
    if not (name and price and unit_measure_id):
        return Response(
            body={
                "message": "Name, price and unit measure id are required",
                "error": "Incorrect request body."
            },
            status_code=400,
        )

    response_data, status_code = create_product(name=name, price=price, unit_measure_id=unit_measure_id)
    return Response(
        body=response_data,
        status_code=status_code,
    )


@product_routes.route('/product/{id}', methods=['GET'])
def get_product_by_id(id):
    get_product, status_code = filter_product_by_id(id=id)
    return Response(
        body=get_product,
        status_code=status_code,
    )


@product_routes.route('/product/{id}', methods=['PUT'])
def update_product_by_id(id):
    data = product_routes.current_request.json_body
    name = data.get('name')
    price = data.get('price')
    unit_measure_id = data.get('unit_measure_id')
    if not (name and price and unit_measure_id):
        return Response(
            body={
                "message": "Name, price and unit measure id are required",
                "error": "Incorrect request body."
            },
            status_code=400,
        )

    response_data, status_code = update_product(id=id, name=name, price=price, unit_measure_id=unit_measure_id)
    return Response(
        body=response_data,
        status_code=status_code,
    )


@product_routes.route('/product/{id}', methods=['DELETE'])
def delete_product_by_id(id):
    response_data, status_code = delete_product(id=id)
    return Response(
        body=response_data,
        status_code=status_code,
    )

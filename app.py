from chalice import Chalice, Response
from chalicelib.controllers.unit_measure_controller import (
    list_unit_measure, create_unit_measure, filter_unit_measure_by_id, update_unit_measure,
    update_unit_measure, delete_unit_measure
)
from chalicelib.controllers.products_controller import (
    list_product, create_product, filter_product_by_id
)

app = Chalice(app_name='challenge')

@app.route('/')
def index():
    return {'Welcome': 'API Challenge'}


@app.route('/unit-measure', methods=['GET'])
def get_all_unit_measure():
    get_unit_measure, status_code = list_unit_measure()
    return Response(
        body=get_unit_measure,
        status_code=status_code,
    )


@app.route('/unit-measure', methods=['POST'])
def add_unit_measure():
    data = app.current_request.json_body
    name = data.get('name')
    if not (name):
        return Response(
            body={
                "message": "Name factor are required",
                "error": "Incorrect request body."
            },
            status_code=400,
        )

    response_data, status_code = create_unit_measure(name=name)
    return Response(
        body=response_data,
        status_code=status_code,
    )


@app.route('/unit-measure/{id}', methods=['GET'])
def get_unit_measure_by_id(id):
    get_unit_measure, status_code = filter_unit_measure_by_id(id=id)
    return Response(
        body=get_unit_measure,
        status_code=status_code,
    )


@app.route('/unit-measure/{id}', methods=['PUT'])
def update_unit_measure_by_id(id):
    data = app.current_request.json_body
    name = data.get('name')
    if not (name):
        return Response(
            body={'error': 'Name factor are required.'},
            status_code=400,
        )

    response_data, status_code = update_unit_measure(id=id, name=name)
    return Response(
        body=response_data,
        status_code=status_code,
    )


@app.route('/unit-measure/{id}', methods=['DELETE'])
def delete_unit_measure_by_id(id):
    response_data, status_code = delete_unit_measure(id=id)
    return Response(
        body=response_data,
        status_code=status_code,
    )


# endpoint for product
@app.route('/product', methods=['GET'])
def get_all_product():
    get_product, status_code = list_product()
    return Response(
        body=get_product,
        status_code=status_code,
    )

@app.route('/product', methods=['POST'])
def add_product():
    data = app.current_request.json_body
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


@app.route('/product/{id}', methods=['GET'])
def get_product_by_id(id):
    get_product, status_code = filter_product_by_id(id=id)
    return Response(
        body=get_product,
        status_code=status_code,
    )


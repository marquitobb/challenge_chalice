from chalice import Chalice, Response
from chalicelib.controllers.unit_measure_controller import (
    list_unit_measure, create_unit_measure, filter_unit_measure_by_id, update_unit_measure,
    delete_unit_measure
)
from chalicelib.controllers.products_controller import (
    list_product, create_product, filter_product_by_id, update_product,
    delete_product
)
from chalicelib.controllers.sales_crontoller import (
    list_sale, create_sale, filter_sale_by_id, update_sale,
    delete_sale, get_sales_by_products, get_all_sales_by_products
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


@app.route('/product/{id}', methods=['PUT'])
def update_product_by_id(id):
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

    response_data, status_code = update_product(id=id, name=name, price=price, unit_measure_id=unit_measure_id)
    return Response(
        body=response_data,
        status_code=status_code,
    )


@app.route('/product/{id}', methods=['DELETE'])
def delete_product_by_id(id):
    response_data, status_code = delete_product(id=id)
    return Response(
        body=response_data,
        status_code=status_code,
    )


# endpoint for sale
@app.route('/sale', methods=['GET'])
def get_all_sale():
    get_sale, status_code = list_sale()
    return Response(
        body=get_sale,
        status_code=status_code,
    )


@app.route('/sale', methods=['POST'])
def add_sale():
    data = app.current_request.json_body
    date = data.get('date')
    quantity = data.get('quantity')
    product_id = data.get('product_id')
    if not (date and quantity and product_id):
        return Response(
            body={
                "message": "Date, quantity and product id are required",
                "error": "Incorrect request body."
            },
            status_code=400,
        )

    response_data, status_code = create_sale(date=date, quantity=quantity, product_id=product_id)
    return Response(
        body=response_data,
        status_code=status_code,
    )


@app.route('/sale/{id}', methods=['GET'])
def get_sale_by_id(id):
    get_sale, status_code = filter_sale_by_id(id=id)
    return Response(
        body=get_sale,
        status_code=status_code,
    )


@app.route('/sale/{id}', methods=['PUT'])
def update_sale_by_id(id):
    data = app.current_request.json_body
    date = data.get('date')
    quantity = data.get('quantity')
    product_id = data.get('product_id')
    if not (date and quantity and product_id):
        return Response(
            body={
                "message": "Date, quantity and product id are required",
                "error": "Incorrect request body."
            },
            status_code=400,
        )

    response_data, status_code = update_sale(id=id, date=date, quantity=quantity, product_id=product_id)
    return Response(
        body=response_data,
        status_code=status_code,
    )


@app.route('/sale/{id}', methods=['DELETE'])
def delete_sale_by_id(id):
    response_data, status_code = delete_sale(id=id)
    return Response(
        body=response_data,
        status_code=status_code,
    )


# endpoint for product sales
@app.route('/product-sales', methods=['GET'])
def get_product_sales():
    response_data, status_code = get_sales_by_products()
    return Response(
        body=response_data,
        status_code=status_code,
    )


# endpoint for total sales
@app.route('/total-sales', methods=['GET'])
def get_sales():
    response_data, status_code = get_all_sales_by_products()
    return Response(
        body=response_data,
        status_code=status_code,
    )

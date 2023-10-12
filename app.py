from chalice import Chalice, Response
from chalicelib.controllers.sale_crontoller import (
    list_sale, create_sale, filter_sale_by_id, update_sale,
    delete_sale, get_sales_by_products, get_all_sales_by_products
)
from chalicelib.routes import unit_measure_route, product_route


app = Chalice(app_name='challenge')
app.register_blueprint(unit_measure_route.unit_measure_routes)
app.register_blueprint(product_route.product_routes)

@app.route('/')
def index():
    return {'Welcome': 'API Challenge'}


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

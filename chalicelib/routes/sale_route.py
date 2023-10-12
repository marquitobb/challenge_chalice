from chalice import Blueprint, Response
from chalicelib.controllers.sale_crontoller import (
    list_sale, create_sale, filter_sale_by_id, update_sale,
    delete_sale, get_sales_by_products, get_all_sales_by_products
)

sale_routes = Blueprint(__name__)

# endpoint for sale
@sale_routes.route('/sale', methods=['GET'])
def get_all_sale():
    get_sale, status_code = list_sale()
    return Response(
        body=get_sale,
        status_code=status_code,
    )


@sale_routes.route('/sale', methods=['POST'])
def add_sale():
    data = sale_routes.current_request.json_body
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


@sale_routes.route('/sale/{id}', methods=['GET'])
def get_sale_by_id(id):
    get_sale, status_code = filter_sale_by_id(id=id)
    return Response(
        body=get_sale,
        status_code=status_code,
    )


@sale_routes.route('/sale/{id}', methods=['PUT'])
def update_sale_by_id(id):
    data = sale_routes.current_request.json_body
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


@sale_routes.route('/sale/{id}', methods=['DELETE'])
def delete_sale_by_id(id):
    response_data, status_code = delete_sale(id=id)
    return Response(
        body=response_data,
        status_code=status_code,
    )


# endpoint for product sales
@sale_routes.route('/product-sales', methods=['GET'])
def get_product_sales():
    response_data, status_code = get_sales_by_products()
    return Response(
        body=response_data,
        status_code=status_code,
    )


# endpoint for total sales
@sale_routes.route('/total-sales', methods=['GET'])
def get_sales():
    response_data, status_code = get_all_sales_by_products()
    return Response(
        body=response_data,
        status_code=status_code,
    )

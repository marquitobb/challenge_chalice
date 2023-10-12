from chalicelib.models.models import Sale, Session, Product
from sqlalchemy import func
from chalicelib.utils.general_response import GeneralResponse

SALE_NOT_FOUND = "Sale not found."
NOT_FOUND = "Not Found."
SALE_FOUND = "Sale found."


def list_sale() -> dict and int:
    session = Session()
    try:
        get_all_sale = list()
        get_sale = session.query(Sale).all()
        for item in get_sale:
            get_all_sale.append({
                "id": item.id,
                "date": item.date.strftime("%Y-%m-%d"),
                "quantity": item.quantity,
                "product_id": item.product_id,
                "product": {
                    "id": item.product.id,
                    "name": item.product.name,
                    "price": item.product.price,
                    "unit_measure_id": item.product.unit_measure_id,
                    "unit_measure": {
                        "id": item.product.unit_measure.id,
                        "name": item.product.unit_measure.name
                    }
                }
            })
        return GeneralResponse.success(data=get_all_sale, message=SALE_FOUND)
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


def create_sale(date: str, quantity: int, product_id: int) -> dict and int:
    session = Session()
    try:
        sale = Sale(date=date, quantity=quantity, product_id=product_id)
        session.add(sale)
        session.commit()
        return GeneralResponse.success(message="Sale created.", status_code=201)
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


def filter_sale_by_id(id: int) -> dict and int:
    session = Session()
    try:
        get_sale = session.query(Sale).filter(Sale.id == id).first()
        if not get_sale:
            return GeneralResponse.error(message=SALE_NOT_FOUND, type_error=NOT_FOUND, status_code=404)
        data={
            "id": get_sale.id,
            "date": get_sale.date.strftime("%Y-%m-%d"),
            "quantity": get_sale.quantity,
            "product_id": get_sale.product_id,
            "product": {
                "id": get_sale.product.id,
                "name": get_sale.product.name,
                "price": get_sale.product.price,
                "unit_measure_id": get_sale.product.unit_measure_id,
                "unit_measure": {
                    "id": get_sale.product.unit_measure.id,
                    "name": get_sale.product.unit_measure.name
                }
            }
        }
        return GeneralResponse.success(data=data, message=SALE_FOUND)
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


def update_sale(id: int, date: str, quantity: int, product_id: int) -> dict and int:
    session = Session()
    try:
        get_sale = session.query(Sale).filter(Sale.id == id).first()
        if not get_sale:
            return GeneralResponse.error(message=SALE_NOT_FOUND, type_error=NOT_FOUND, status_code=404)
        get_sale.date = date
        get_sale.quantity = quantity
        get_sale.product_id = product_id
        session.commit()
        return GeneralResponse.success(message="Sale updated.")
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


def delete_sale(id: int) -> dict and int:
    session = Session()
    try:
        get_sale = session.query(Sale).filter(Sale.id == id).first()
        if not get_sale:
            return GeneralResponse.error(message=SALE_NOT_FOUND, type_error=NOT_FOUND, status_code=404)
        session.delete(get_sale)
        session.commit()
        return GeneralResponse.success(message="Sale deleted.")
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


# filter sales to products
def get_sales_by_products() -> dict and int:
    session = Session()
    try:
        list_each_product = list()

        # filter each product and sum the total sales and total price
        sales_by_product = session.query(
            Product.name,
            func.sum(Sale.quantity).label('total_sales'),
            func.sum(Sale.quantity * Product.price).label('total_price')
        ).join(Sale).group_by(Product.name).all()

        # append the data to a list
        for item in sales_by_product:
            list_each_product.append({
                "name": item.name,
                "total_sales": item.total_sales,
                "total_price": item.total_price
            })

        return GeneralResponse.success(data=list_each_product, message="Sale found.")
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


# filter the sales of all products
def get_all_sales_by_products() -> dict and int:
    session = Session()
    try:
        get_each_sale_by_product = get_sales_by_products()

        # declare a dict to store the total sales and total price
        data = {
            "total_sales": 0,
            "total_price": 0
        }

        # sum the total sales and total price of each product
        for item in get_each_sale_by_product[0]["data"]:
            data["total_sales"] += item["total_sales"]
            data["total_price"] += item["total_price"]

        return GeneralResponse.success(data=data, message="Sale found.")
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


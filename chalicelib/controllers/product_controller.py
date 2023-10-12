from chalicelib.models.models import Product, Session
from chalicelib.utils.general_response import GeneralResponse

PRODUCT_NOT_FOUND = "Product not found."
NOT_FOUND = "Not Found."


def list_product() -> dict and int:
    """_summary_

    Returns:
        dict and int: return a dict with a list of products and a status code.
    """
    session = Session()
    try:
        get_all_product = list()
        get_product = session.query(Product).all()
        for item in get_product:
            get_all_product.append({
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "unit_measure_id": item.unit_measure_id,
                "unit_measure": {
                    "id": item.unit_measure.id,
                    "name": item.unit_measure.name
                }
            })
        return GeneralResponse.success(data=get_all_product, message="Product found.")
    except Exception as e:
        GeneralResponse.error(message=str(e))
    finally:
        session.close()


def create_product(name: str, price: int, unit_measure_id: int) -> dict and int:
    session = Session()
    try:
        product = Product(name=name, price=price, unit_measure_id=unit_measure_id)
        session.add(product)
        session.commit()
        data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "unit_measure_id": product.unit_measure_id,
            "unit_measure": {
                "id": product.unit_measure.id,
                "name": product.unit_measure.name
            }
        }
        return GeneralResponse.success(data=data, message="Product created.", status_code=201)
    except Exception as e:
        GeneralResponse.error(message=str(e))
    finally:
        session.close()


def filter_product_by_id(id: int) -> dict and int:
    session = Session()
    try:
        get_product = session.query(Product).filter_by(id=id).first()
        if not get_product:
            return GeneralResponse.error(message=PRODUCT_NOT_FOUND, error_type=NOT_FOUND, status_code=404)
        data = {
            "id": get_product.id,
            "name": get_product.name,
            "price": get_product.price,
            "unit_measure_id": get_product.unit_measure_id,
            "unit_measure": {
                "id": get_product.unit_measure.id,
                "name": get_product.unit_measure.name
            }
        }
        return GeneralResponse.success(data=data, message="Product found.")
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


def update_product(id: int, name: str, price: int, unit_measure_id: int) -> dict and int:
    session = Session()
    try:
        get_product = session.query(Product).filter_by(id=id).first()
        if not get_product:
            return GeneralResponse.error(message=PRODUCT_NOT_FOUND, error_type=NOT_FOUND, status_code=404)
        get_product.name = name
        get_product.price = price
        get_product.unit_measure_id = unit_measure_id
        session.commit()
        data = {
            "id": get_product.id,
            "name": get_product.name,
            "price": get_product.price,
            "unit_measure_id": get_product.unit_measure_id,
            "unit_measure": {
                "id": get_product.unit_measure.id,
                "name": get_product.unit_measure.name
            }
        }
        return GeneralResponse.success(data=data, message="Product updated.")
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


def delete_product(id: int) -> dict and int:
    session = Session()
    try:
        get_product = session.query(Product).filter_by(id=id).first()
        if not get_product:
            return GeneralResponse.error(message=PRODUCT_NOT_FOUND, error_type=NOT_FOUND, status_code=404)
        session.delete(get_product)
        session.commit()
        return GeneralResponse.success(message="Product deleted.")
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


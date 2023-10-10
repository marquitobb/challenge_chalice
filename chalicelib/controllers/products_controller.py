from chalicelib.models.models import Product, Session


def list_product() -> dict and int:
    try:
        get_all_product = list()
        session = Session()
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
        session.close()
        return {
            "data": get_all_product,
            "message": "Product found."
        }, 200
    except Exception as e:
        return {
            "message": str(e),
            "error": "Internal Server Error"
        }, 500


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
        return {
            "data": data,
            "message": "Product created."
        }, 201
    except Exception as e:
        return {
            "message": str(e),
            "error": "Internal Server Error"
        }, 500
    finally:
        session.close()


def filter_product_by_id(id: int) -> dict and int:
    session = Session()
    try:
        get_product = session.query(Product).filter_by(id=id).first()
        if not get_product:
            return {
                "message": "Product not found.",
                "error": "Not Found."
            }, 404
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
        return {
            "data": data,
            "message": "Product found."
        }, 200
    except Exception as e:
        return {
            "message": str(e),
            "error": "Internal Server Error"
        }, 500
    finally:
        session.close()
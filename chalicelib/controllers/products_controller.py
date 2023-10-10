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


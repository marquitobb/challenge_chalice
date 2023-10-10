from chalicelib.models.models import UnitMeasure, Session


def create_unit_measure(name: str) -> dict and int:
    try:
        session = Session()
        unit_measure = UnitMeasure(name=name)
        session.add(unit_measure)
        session.commit()
        session.refresh(unit_measure)
        session.close()
        return {
            "message": "Unit Measure created successfully.",
            "data": {
                "id": unit_measure.id,
                "name": unit_measure.name
            }
        }, 201
    except Exception as e:
        return {
            "message": str(e),
            "error": "Internal Server Error"
        }, 500


def list_unit_measure() -> dict and int:
    try:
        get_all_unit_measure = list()
        session = Session()
        get_unit_measure = session.query(UnitMeasure).all()
        for item in get_unit_measure:
            get_all_unit_measure.append({
                "id": item.id,
                "name": item.name
            })
        session.close()
        return {
            "data": get_all_unit_measure,
            "message": "Unit Measure found."
        }, 200
    except Exception as e:
        return {
            "message": str(e),
            "error": "Internal Server Error"
        }, 500


def filter_unit_measure_by_id(id: int) -> dict and int:
    session = Session()
    get_unit_measure = session.query(UnitMeasure).filter(UnitMeasure.id == id).first()
    session.close()
    if get_unit_measure:
        return {
            "data": {
                "id": get_unit_measure.id,
                "name": get_unit_measure.name
            },
            "message": "Unit Measure found."
        }, 200
    else:
        return {
            "message": "Unit Measure not found.",
            "error": "Not Found"
        }, 404


def update_unit_measure(id: int, name: str) -> dict and int:
    try:
        session = Session()
        get_unit_measure = session.query(UnitMeasure).filter(UnitMeasure.id == id).first()
        if get_unit_measure:
            get_unit_measure.name = name
            session.commit()
            session.refresh(get_unit_measure)
            session.close()
            return {
                "data": {
                    "id": get_unit_measure.id,
                    "name": get_unit_measure.name
                },
                "message": "Unit Measure updated successfully."
            }, 200
        else:
            return {
                "message": "Unit Measure not found.",
                "error": "Not Found"
            }, 404
    except Exception as e:
        return {
            "message": str(e),
            "error": "Internal Server Error"
        }, 500


def delete_unit_measure(id: int) -> dict and int:
    try:
        session = Session()
        get_unit_measure = session.query(UnitMeasure).filter(UnitMeasure.id == id).first()
        if get_unit_measure:
            session.delete(get_unit_measure)
            session.commit()
            session.close()
            return {
                "message": "Unit Measure deleted successfully."
            }, 200
        else:
            return {
                "message": "Unit Measure not found.",
                "error": "Not Found"
            }, 404
    except Exception as e:
        return {
            "message": str(e),
            "error": "Internal Server Error"
        }, 500
from chalicelib.models.unit_measure_model import UnitMeasure, Session


def create_unit_measure(
    name: str,
) -> dict and int:
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


def list_unit_measure() -> list:
    get_all_unit_measure = list()
    session = Session()
    get_unit_measure = session.query(UnitMeasure).all()
    for item in get_unit_measure:
        get_all_unit_measure.append({
            "id": item.id,
            "name": item.name
        })
    session.close()
    return get_all_unit_measure
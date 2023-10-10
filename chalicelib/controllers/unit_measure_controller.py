from chalicelib.models.unit_measure_model import UnitMeasure, Session


def create_unit_measure(
    name: str,
) -> dict:
    return "test"


def list_unit_measure() -> list:
    get_all_unit_measure = list()
    session = Session()
    resultados = session.query(UnitMeasure).all()
    for resultado in resultados:
        get_all_unit_measure.append({
            "id": resultado.id,
            "name": resultado.name
        })
    session.close()
    return get_all_unit_measure
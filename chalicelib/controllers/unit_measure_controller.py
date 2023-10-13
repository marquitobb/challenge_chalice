from chalicelib.models.models import UnitMeasure, Session
from chalicelib.utils.general_response import GeneralResponse

UNIT_MEASURE_NOT_FOUND = "Unit Measure not found."
NOT_FOUND = "Not Found."

def create_unit_measure(name: str) -> dict and int:
    session = Session()
    try:
        unit_measure = UnitMeasure(name=name)
        session.add(unit_measure)
        session.commit()
        session.refresh(unit_measure)
        data= {
            "id": unit_measure.id,
            "name": unit_measure.name
        }
        return GeneralResponse.success(data=data, message="Unit Measure created.", status_code=201)
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


def list_unit_measure() -> dict and int:
    session = Session()
    try:
        get_all_unit_measure = list()
        get_unit_measure = session.query(UnitMeasure).all()
        for item in get_unit_measure:
            get_all_unit_measure.append({
                "id": item.id,
                "name": item.name
            })
        return GeneralResponse.success(data=get_all_unit_measure, message="Unit Measure found.")
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


def filter_unit_measure_by_id(id: int) -> dict and int:
    session = Session()
    try:
        get_unit_measure = session.query(UnitMeasure).filter(UnitMeasure.id == id).first()
        if not get_unit_measure:
            return GeneralResponse.error(message=UNIT_MEASURE_NOT_FOUND, type_error=NOT_FOUND, status_code=404)
        data= {
            "id": get_unit_measure.id,
            "name": get_unit_measure.name
        },
        return GeneralResponse.success(data=data, message="Unit Measure found.")
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


def update_unit_measure(id: int, name: str) -> dict and int:
    session = Session()
    try:
        get_unit_measure = session.query(UnitMeasure).filter(UnitMeasure.id == id).first()
        if not get_unit_measure:
            return GeneralResponse.error(message=UNIT_MEASURE_NOT_FOUND, type_error=NOT_FOUND, status_code=404)
        get_unit_measure.name = name
        session.commit()
        session.refresh(get_unit_measure)
        data= {
            "id": get_unit_measure.id,
            "name": get_unit_measure.name
        },
        return GeneralResponse.success(data=data, message="Unit Measure updated successfully.")
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()


def delete_unit_measure(id: int) -> dict and int:
    session = Session()
    try:
        get_unit_measure = session.query(UnitMeasure).filter(UnitMeasure.id == id).first()
        if not get_unit_measure:
            return GeneralResponse.error(message=UNIT_MEASURE_NOT_FOUND, type_error=NOT_FOUND, status_code=404)
        session.delete(get_unit_measure)
        session.commit()
        return GeneralResponse.success(message="Unit Measure deleted successfully.")
    except Exception as e:
        return GeneralResponse.error(message=str(e))
    finally:
        session.close()
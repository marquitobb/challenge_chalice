from chalice import Blueprint, Response
from chalicelib.controllers.unit_measure_controller import (
    list_unit_measure, create_unit_measure, filter_unit_measure_by_id, update_unit_measure,
    delete_unit_measure
)


unit_measure_routes = Blueprint(__name__)


@unit_measure_routes.route('/unit-measure', methods=['GET'])
def get_all_unit_measure():
    get_unit_measure, status_code = list_unit_measure()
    return Response(
        body=get_unit_measure,
        status_code=status_code,
    )


@unit_measure_routes.route('/unit-measure', methods=['POST'])
def add_unit_measure():
    data = unit_measure_routes.current_request.json_body
    name = data.get('name')
    if not (name):
        return Response(
            body={
                "message": "Name factor are required",
                "error": "Incorrect request body."
            },
            status_code=400,
        )

    response_data, status_code = create_unit_measure(name=name)
    return Response(
        body=response_data,
        status_code=status_code,
    )


@unit_measure_routes.route('/unit-measure/{id}', methods=['GET'])
def get_unit_measure_by_id(id):
    get_unit_measure, status_code = filter_unit_measure_by_id(id=id)
    return Response(
        body=get_unit_measure,
        status_code=status_code,
    )


@unit_measure_routes.route('/unit-measure/{id}', methods=['PUT'])
def update_unit_measure_by_id(id):
    data = unit_measure_routes.current_request.json_body
    name = data.get('name')
    if not (name):
        return Response(
            body={'error': 'Name factor are required.'},
            status_code=400,
        )

    response_data, status_code = update_unit_measure(id=id, name=name)
    return Response(
        body=response_data,
        status_code=status_code,
    )


@unit_measure_routes.route('/unit-measure/{id}', methods=['DELETE'])
def delete_unit_measure_by_id(id):
    response_data, status_code = delete_unit_measure(id=id)
    return Response(
        body=response_data,
        status_code=status_code,
    )

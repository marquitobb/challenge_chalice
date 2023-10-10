from chalice import Chalice, Response
from chalicelib.controllers.unit_measure_controller import list_unit_measure, create_unit_measure

app = Chalice(app_name='challenge')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/unit-measure', methods=['GET'])
def get_all_unit_measure():
    return {"data": list_unit_measure()}


@app.route('/unit-measure', methods=['POST'])
def get_all_unit_measure():
    data = app.current_request.json_body
    name = data.get('name')
    if not (name):
        return Response(
            body={'error': 'Name factor are required.'},
            status_code=400,
        )

    response_data, status_code = create_unit_measure(name=name)
    return Response(
        body=response_data,
        status_code=status_code,
    )


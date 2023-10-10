from chalice import Chalice
from chalicelib.controllers.unit_measure_controller import list_unit_measure

app = Chalice(app_name='challenge')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/unit-measure', methods=['GET'])
def get_all_unit_measure():
    return {"data": list_unit_measure()}
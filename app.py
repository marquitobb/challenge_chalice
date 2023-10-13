from chalice import Chalice
from chalicelib.routes import unit_measure_route, product_route, sale_route


app = Chalice(app_name='challenge')
app.register_blueprint(unit_measure_route.unit_measure_routes)
app.register_blueprint(product_route.product_routes)
app.register_blueprint(sale_route.sale_routes)

@app.route('/')
def index():
    return {'Welcome': 'API Challenge'}

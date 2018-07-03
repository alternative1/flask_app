import json
#import time
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.catalog.models import Product

catalog = Blueprint('catalog', __name__)

#d = datatime.timedelta
string =  "Welcome to my RESTful App! \n Please, make a request from my database of plants \n I need to sleep"

@catalog.route('/')
@catalog.route('/home')
def home():
    return string #"Welcome to my RESTful App! \n Please, make a request from my database of plants \n I need to sleep"
    #"Please, make a request from my database of plants"
    #"The current time is:"
    #time.localtime( time.time() )


class ProductView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            products = Product.query.paginate(page, 10).items
            res = {}
            for product in products:
                res[product.id] = {
                    'name': product.name,
                    'price': str(product.price),
                }
        else:
            product = Product.query.filter_by(id=id).first()
            if not product:
                abort(404)
            res = {
                'name': product.name,
                'price': str(product.price),
            }
        return jsonify(res)

    def post(self):
        name = request.form.get('name')
        price = request.form.get('price')
        product = Product(name, price)
        db.session.add(product)
        db.session.commit()
        return jsonify({product.id: {
            'name': product.name,
            'price': str(product.price),
        }})

    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return

    def delete(self, id):
        # Delete the record for the provided id.
        return


product_view =  ProductView.as_view('product_view')
app.add_url_rule(
    '/product/', view_func=product_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/product/<int:id>', view_func=product_view, methods=['GET']
)

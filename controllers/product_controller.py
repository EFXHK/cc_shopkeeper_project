from flask import Flask, render_template
from flask import Blueprint

from models.product import Product
from models.maker import Maker

import repositories.maker_repository as maker_repository
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)
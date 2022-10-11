from flask import Flask, render_template, request, redirect
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

################################################################

@products_blueprint.route("/products/new", methods=['GET'])
def new_product():
    products = product_repository.select_all()
    ############ makers = makers_repository.select_all()
    return render_template("products/new.html", products = products)



################################################################

@products_blueprint.route("/products/<id>")
def show(id):
    product = product_repository.select(id)
    maker = product_repository.makers(product)
    return render_template("products/show.html", product=product, maker=maker)

@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def edit_product(id):
    product = product_repository.select(id)
    maker = maker_repository.select_all()
    return render_template("product/edit.html", product=product, maker=maker)

@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')

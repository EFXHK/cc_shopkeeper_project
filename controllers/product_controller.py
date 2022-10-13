# from unicodedata import name
from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.product import Product
from models.maker import Maker

import repositories.maker_repository as maker_repository
import repositories.product_repository as product_repository  # Keep an eye on the order

products_blueprint = Blueprint("products", __name__)


@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products) # this could go into /  and homepage

################################################################

@products_blueprint.route("/products/new", methods=['GET']) 
def new_product():
    products = product_repository.select_all()
    makers = maker_repository.select_all() 
    return render_template("products/new.html", products = products, makers = makers)

@products_blueprint.route("/products", methods=['POST'])
def add_product():
    ### would ID be in here? isnt ID automatically generated? 
    name = request.form['name']
    purchase = request.form['purchase']
    sell = request.form['sell']
    description = request.form['description']
    stock_qty = request.form['stock_qty']

    maker_id = request.form['maker_id']
    maker = maker_repository.select(maker_id)
    product = Product(name, purchase, sell, description, stock_qty, maker)
    product_repository.save(product)
    return redirect("/products")

################################################################

@products_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template("products/show.html", product=product)

@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def edit_product(id):
#   products = product_repository.select(id)
#   maker = maker_repository.select_all()
    return render_template("products/edit.html", 
                        product = product_repository.select(id),
                        makers = maker_repository.select_all())

@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')

@products_blueprint.route("/products/<id>", methods=['POST'])
def update_product(id):
    name        = request.form['name']
    purchase    = request.form['purchase']
    sell        = request.form['sell']
    description = request.form['description']
    stock_qty   = request.form['stock_qty']
    maker       = maker_repository.select(request.form['maker_id'])
    product     = Product(name, purchase, sell, description, stock_qty, maker, id) # sus
    # product     = product_repository.select(maker)
    product_repository.update(product)
    return redirect("/products")



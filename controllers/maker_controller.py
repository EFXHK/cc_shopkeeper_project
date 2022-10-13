#from itertools import product
from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.product import Product
from models.maker import Maker

import repositories.maker_repository as maker_repository
import repositories.product_repository as product_repository

makers_blueprint = Blueprint("makers", __name__)

@makers_blueprint.route("/makers")
def makers():
    makers = maker_repository.select_all()
    return render_template("makers/index.html", makers = makers)

# @makers_blueprint.route("/makers")
# def makers():
#     makers = maker_repository.select_all()
#     return render_template("makers/index.html", makers = makers)

@makers_blueprint.route("/makers/new", methods=['GET'])
def new_maker():
    makers = maker_repository.select_all()
    products = product_repository.select_all()
    return render_template("makers/new.html", makers = makers, products = products)

# CREATE, POST /makers
@makers_blueprint.route("/makers", methods=['POST'])
def create_maker():
    name        = request.form['name']
    address     = request.form['address']
    maker       = Maker(name, address)
    maker_repository.save(maker)
    return redirect("/makers")

#####################################################################
#### this is for editing

@makers_blueprint.route("/makers/<id>", methods=['POST'])
def update_makers(id):
    name        = request.form['name']
    address     = request.form['address']
    maker       = maker_repository.select(maker)
    maker       = Maker(name, address, id)
    maker_repository.update(maker)
    return redirect("/makers")

#####################################################################

@makers_blueprint.route("/makers/<id>/delete", methods=['POST'])
def delete_maker(id):
    maker_repository.delete(id)
    return redirect("/makers")









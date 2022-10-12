from itertools import product
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
    name = request.form['name'] # this is probably wrong?
    address = request.form['address'] # i dont understand how to do this one
    maker_repository.save(makers)
    return redirect("/makers")
# do i need to append to a list?

@makers_blueprint.route("makers/<id>/delete", methods=['POST'])
def delete_maker(id):
    maker_repository.delete(id)
    return redirect("/makers")









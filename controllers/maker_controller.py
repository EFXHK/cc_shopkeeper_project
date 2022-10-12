from flask import Flask, render_template, request, redirect
from flask import Blueprint

# from models.product import Product
from models.maker import Maker

import repositories.maker_repository as maker_repository
# import repositories.product_repository as product_repository

makers_blueprint = Blueprint("makers", __name__)

# makers_blueprint = Blueprint("makers", __name__)

@makers_blueprint.route("/makers")
def makers():
    makers = maker_repository.select_all()
    return render_template("makers/index.html", makers = makers)

# @makers_blueprint.route("/makers")
# def makers():
#     makers = maker_repository.select_all()
#     return render_template("makers/index.html", makers = makers)

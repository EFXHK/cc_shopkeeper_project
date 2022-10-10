# from multiprocessing import AuthenticationError
from db.run_sql import run_sql

from models.maker import Maker  # 1.2many
from models.product import Product

# SAVE

def save(maker):
    sql = """
    INSERT INTO maker (name, address)
    VALUES (%s %s) RETURNING *
    """
    values = [maker.name, maker.address]
    results = run_sql(sql, values)
    #id = results[0]['id']     # explain again
    #maker.id = id
    maker.id = results[0]['id']
    return maker


# add rest of functions

def delete_all():
    sql = "DELETE FROM maker"
    run_sql(sql)
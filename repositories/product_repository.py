from db.run_sql import run_sql

from models.product import Product
from models.maker import Maker

# SAVE

def save(product):
    sql = """
    INSERT INTO products (name, purchase, sell, description, stock_qty)
    VALUES (%s, %s, %s, %s, %s)  RETURNING *
    """
    values = [product.name, product.purchase, product.sell, product.description, product.stock_qty]
    results = run_sql(sql, values)
    #id = results[0]['id']
    #product.id = id
    product.id = results[0]['id']
    return product

# SELECT ALL, ID / DELETE ALL, ID / UPDATE

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

#this is delete ID ONLY
# def delete(id):
#     sql = "DELETE FROM product WHERE id = %s"
#     values = [id]
#     run_sql(sql,values)

from db.run_sql import run_sql
from repositories import maker_repository
from models.product import Product
from models.maker import Maker

# SAVE
### missing empty list?
def save(product):
    sql = """
    INSERT INTO products (name, purchase, sell, description, stock_qty, maker_id)
    VALUES (%s, %s, %s, %s, %s, %s)  RETURNING *
    """
    values = [product.name, product.purchase, product.sell, product.description, product.stock_qty, product.maker.id] #nested
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    # product.id = results[0]['id']
    return product

# SELECT ALL, ID / DELETE ALL, ID / UPDATE


def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        maker = maker_repository.select(row['maker_id'])
        product = Product(row['name'], row['purchase'], row['sell'], row['description'], row['stock_qty'], maker, row['id'])
        products.append(product)
    return products

# def select(id):
#     user = None
#     sql = "SELECT * FROM products WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)

#     if results:
#         result = results[0]
#         product = Product(result['name'], result['purchase'], result['sell'], result['description'], result['stock_qty'], result['maker'], result['id'])
#     return product



def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)


# #this is delete ID ONLY
# def delete(id):
#     sql = "DELETE FROM product WHERE id = %s"
#     values = [id]
#     run_sql(sql,values)

# def update(product):
#     sql = "UPDATE products SET (name, purchase, sell, description, stock_qty, maker) = (%s, %s, %s, %s, %s, %s) WHERE is = %s"
#     values = [product.name, product. purchase, product.sell, product.description, product.stock_qty, product.maker, product.id]
#     run_sql(sql, values)

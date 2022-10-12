class Product:
    def __init__(self, name, purchase, sell, description, stock_qty, maker, id = None):
        self.name = name
        self.purchase = purchase
        self.sell = sell
        self.description = description
        self.stock_qty = stock_qty
        self.maker = maker
        self.id = id

    def out_of_stock(self):
        if self.stock_qty == 0:
            return True

    ## need to print something?
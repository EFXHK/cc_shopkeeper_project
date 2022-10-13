class Product:
    def __init__(self, name, purchase, sell, description, stock_qty, maker, id = None):
        self.name = name
        self.purchase = purchase
        self.sell = sell
        self.description = description
        self.stock_qty = stock_qty
        self.maker = maker
        self.id = id



    def get_stock_level(self):
        if self.stock_qty == 0:
            return "Zero Stock"
        elif self.stock_qty <= 2:  # if if also fine
            return "Low Stock"
        else:
            return ""      # with or without else does the same and is fine

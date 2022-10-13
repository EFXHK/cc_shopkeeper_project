import pdb
from models.product import Product
from models.maker import Maker

import repositories.product_repository as product_repository
import repositories.maker_repository as maker_repository

product_repository.delete_all()
maker_repository.delete_all()


# DB

makerX1 = Maker("Siegwards Brewery", "33 Catarina Crescent")
maker_repository.save(makerX1)

makerX2 = Maker("Sage's Hat", "Farron Keep, 2nd Floor")
maker_repository.save(makerX2)

productX1 = Product("Siegbrau", 18, 27, "Comes in a jolly barrel mug.", 60, makerX1)
product_repository.save(productX1)

productX2 = Product("Estus Flask", 298, 523, "It is warm to the touch.", 1, makerX1)
product_repository.save(productX2)

productX3 = Product("Moonlight Arrow (x10)", 55, 78, "(Bow sold separately).", 150, makerX2)
product_repository.save(productX3)


all_makers = maker_repository.select_all()
all_products = product_repository.select_all()

for maker in all_makers:
    print(maker.__dict__)

for product in all_products:
    print(product.__dict__)

# pdb.set_trace() # inserts debugger
breakpoint()

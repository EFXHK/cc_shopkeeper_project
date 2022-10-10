import pdb
from models.product import Product
from models.maker import Maker

import repositories.product_repository as product_repository
import repositories.maker_repository as maker_repository

product_repository.delete_all()
maker_repository.delete_all()

productX1 = Product("Siegbrau", 18, 27, "Comes in a jolly barrel mug", 60)
product_repository.save(productX1)

makerX1 = Maker("Siegwards Brewery", "33 Catarina Crescent")
maker_repository.save(makerX1)

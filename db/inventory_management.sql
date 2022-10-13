DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS makers;


CREATE TABLE makers (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    address VARCHAR (255)
);


CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    purchase FLOAT, 
    sell FLOAT,
    description VARCHAR (255),
    stock_qty INT,
--  maker VARCHAR (255),
    maker_id INT NOT NULL REFERENCES makers(id) --ON DELETE CASCADE
    --review TEXT
);


-- numbers = "{:,}".format(500000)
-- print(numbers)
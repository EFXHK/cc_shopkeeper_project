DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS makers;


CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    purchase FLOAT,
    sell FLOAT,
    description VARCHAR (255),
    stock_qty INT,
    maker_id INT NOT NULL REFERENCES makers(id) -- makerS?
);

CREATE TABLE makers (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    address VARCHAR (255)
);


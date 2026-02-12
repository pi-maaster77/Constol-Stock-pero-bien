
CREATE TABLE move (
	id SERIAL NOT NULL, 
	date DATE, 
	PRIMARY KEY (id)
)



CREATE TABLE unit (
	id SERIAL NOT NULL, 
	name VARCHAR NOT NULL, 
	abreviation VARCHAR NOT NULL, 
	PRIMARY KEY (id)
)



CREATE TABLE product (
	id SERIAL NOT NULL, 
	bc VARCHAR NOT NULL, 
	name VARCHAR NOT NULL, 
	ammount INTEGER NOT NULL, 
	expires BOOLEAN NOT NULL, 
	price_cache FLOAT, 
	active BOOLEAN NOT NULL, 
	price_formula VARCHAR(4) NOT NULL, 
	public_price FLOAT NOT NULL, 
	unit_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(unit_id) REFERENCES unit (id)
)



CREATE TABLE batch (
	id SERIAL NOT NULL, 
	id_product INTEGER NOT NULL, 
	received_at DATE NOT NULL, 
	expires_at DATE, 
	ammount INTEGER NOT NULL, 
	cost_price FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id_product) REFERENCES product (id)
)



CREATE TABLE bulk_discount (
	id SERIAL NOT NULL, 
	id_product INTEGER NOT NULL, 
	min_ammount INTEGER NOT NULL, 
	discount FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	CONSTRAINT unique_discount_rule UNIQUE (id_product, min_ammount), 
	FOREIGN KEY(id_product) REFERENCES product (id)
)



CREATE TABLE move_detail (
	id SERIAL NOT NULL, 
	id_move INTEGER NOT NULL, 
	id_product INTEGER NOT NULL, 
	product_name VARCHAR NOT NULL, 
	ammount INTEGER NOT NULL, 
	unit_price FLOAT NOT NULL, 
	unit_price_final FLOAT NOT NULL, 
	discount_percent FLOAT NOT NULL, 
	discount_amount FLOAT NOT NULL, 
	subtotal FLOAT NOT NULL, 
	total FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id_move) REFERENCES move (id), 
	FOREIGN KEY(id_product) REFERENCES product (id)
)



CREATE TABLE move (
	id SERIAL NOT NULL, 
	date DATE, 
	PRIMARY KEY (id)
)



CREATE TABLE unit (
	id SERIAL NOT NULL, 
	name VARCHAR NOT NULL, 
	abreviation VARCHAR NOT NULL, 
	PRIMARY KEY (id)
)



CREATE TABLE product (
	id SERIAL NOT NULL, 
	bc VARCHAR NOT NULL, 
	name VARCHAR NOT NULL, 
	ammount INTEGER NOT NULL, 
	expires BOOLEAN NOT NULL, 
	price_cache FLOAT, 
	active BOOLEAN NOT NULL, 
	price_formula VARCHAR(4) NOT NULL, 
	public_price FLOAT NOT NULL, 
	unit_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(unit_id) REFERENCES unit (id)
)



CREATE TABLE batch (
	id SERIAL NOT NULL, 
	id_product INTEGER NOT NULL, 
	received_at DATE NOT NULL, 
	expires_at DATE, 
	ammount INTEGER NOT NULL, 
	cost_price FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id_product) REFERENCES product (id)
)



CREATE TABLE bulk_discount (
	id SERIAL NOT NULL, 
	id_product INTEGER NOT NULL, 
	min_ammount INTEGER NOT NULL, 
	discount FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	CONSTRAINT unique_discount_rule UNIQUE (id_product, min_ammount), 
	FOREIGN KEY(id_product) REFERENCES product (id)
)



CREATE TABLE move_detail (
	id SERIAL NOT NULL, 
	id_move INTEGER NOT NULL, 
	id_product INTEGER NOT NULL, 
	product_name VARCHAR NOT NULL, 
	ammount INTEGER NOT NULL, 
	unit_price FLOAT NOT NULL, 
	unit_price_final FLOAT NOT NULL, 
	discount_percent FLOAT NOT NULL, 
	discount_amount FLOAT NOT NULL, 
	subtotal FLOAT NOT NULL, 
	total FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id_move) REFERENCES move (id), 
	FOREIGN KEY(id_product) REFERENCES product (id)
)



CREATE TABLE move (
	id SERIAL NOT NULL, 
	date DATE, 
	PRIMARY KEY (id)
)



CREATE TABLE unit (
	id SERIAL NOT NULL, 
	name VARCHAR NOT NULL, 
	abreviation VARCHAR NOT NULL, 
	PRIMARY KEY (id)
)



CREATE TABLE product (
	id SERIAL NOT NULL, 
	bc VARCHAR NOT NULL, 
	name VARCHAR NOT NULL, 
	ammount INTEGER NOT NULL, 
	expires BOOLEAN NOT NULL, 
	price_cache FLOAT, 
	active BOOLEAN NOT NULL, 
	price_formula VARCHAR(4) NOT NULL, 
	public_price FLOAT NOT NULL, 
	unit_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(unit_id) REFERENCES unit (id)
)



CREATE TABLE batch (
	id SERIAL NOT NULL, 
	id_product INTEGER NOT NULL, 
	received_at DATE NOT NULL, 
	expires_at DATE, 
	ammount INTEGER NOT NULL, 
	cost_price FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id_product) REFERENCES product (id)
)



CREATE TABLE bulk_discount (
	id SERIAL NOT NULL, 
	id_product INTEGER NOT NULL, 
	min_ammount INTEGER NOT NULL, 
	discount FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	CONSTRAINT unique_discount_rule UNIQUE (id_product, min_ammount), 
	FOREIGN KEY(id_product) REFERENCES product (id)
)



CREATE TABLE move_detail (
	id SERIAL NOT NULL, 
	id_move INTEGER NOT NULL, 
	id_product INTEGER NOT NULL, 
	product_name VARCHAR NOT NULL, 
	ammount INTEGER NOT NULL, 
	unit_price FLOAT NOT NULL, 
	unit_price_final FLOAT NOT NULL, 
	discount_percent FLOAT NOT NULL, 
	discount_amount FLOAT NOT NULL, 
	subtotal FLOAT NOT NULL, 
	total FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id_move) REFERENCES move (id), 
	FOREIGN KEY(id_product) REFERENCES product (id)
)



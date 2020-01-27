#Database Setup Commands
CREATE USER food_shop_user ;
ALTER USER 'food_shop_user'@'localhost' IDENTIFIED BY 'food_shop_user_password';
GRANT ALL PRIVILEGES ON *.* TO 'food_shop_user'@'localhost' IDENTIFIED BY 'food_shop_user_password';


CREATE DATABASE food_shop;


CREATE TABLE food_shop.City (
 id INTEGER  PRIMARY KEY AUTO_INCREMENT,
 name  varchar(50) NOT NULL,
 geo_x float NOT NULL,
 geo_y float NOT NULL);

CREATE TABLE    food_shop.User(
 id           INTEGER  PRIMARY KEY AUTO_INCREMENT,
 first_name   varchar(30 ),
 last_name    varchar(30 ) NOT NULL,
 password     varchar(100) NOT NULL,
 email        varchar(100) NOT NULL,
 phone_number varchar(15 ) NOT NULL,
 UNIQUE (email));

CREATE TABLE food_shop.Address(
 id      INTEGER  PRIMARY KEY AUTO_INCREMENT,
 text    varchar(511) NOT NULL,
 city_id INTEGER NOT NULL,
 user_id INTEGER NOT NULL,
 geo_x    float,
 geo_y    float,
 FOREIGN KEY(city_id) REFERENCES  City (id),
 FOREIGN KEY(user_id) REFERENCES  User (id));

CREATE TABLE food_shop.Category(
 id INTEGER  PRIMARY KEY AUTO_INCREMENT,
 name   TEXT NOT NULL);

CREATE TABLE  food_shop.Discount(
 id    INTEGER PRIMARY KEY AUTO_INCREMENT,
 code    TEXT NOT NULL,
 percent  INTEGER NOT NULL);

CREATE TABLE food_shop.Shop(
 id    INTEGER PRIMARY KEY AUTO_INCREMENT,
 city_id         INTEGER NOT NULL,
 name            varchar(100) NOT NULL,
 min_bill_val    INTEGER NOT NULL,
 about           varchar(511) NOT NULL,
 address_text    varchar(511) NOT NULL,
 geo_x     float,
 geo_y     float,
 FOREIGN KEY   (city_id)     REFERENCES    food_shop.City(id));

CREATE TABLE food_shop.DiscountUserRelation(
 id          INTEGER  PRIMARY KEY AUTO_INCREMENT,
 dis_id      INTEGER NOT NULL,
 user_id     INTEGER ,
 FOREIGN KEY(user_id) REFERENCES User(id),
 FOREIGN KEY(dis_id) REFERENCES Discount(id));

CREATE TABLE food_shop.Food(
 id         INTEGER PRIMARY KEY AUTO_INCREMENT,
 shop_id    INTEGER NOT NULL,
 cat_id     INTEGER ,
 price      INTEGER NOT NULL,
 name       varchar(100),
 discount   INTEGER NOT NULL,
 about      varchar(511),
 FOREIGN KEY(cat_id) REFERENCES food_shop.Category (id),
 FOREIGN KEY(shop_id) REFERENCES food_shop.Shop (id));

CREATE TABLE food_shop.FoodUserRelation(
 id INTEGER  PRIMARY KEY AUTO_INCREMENT,
 user_id   INTEGER NOT NULL,
 food_id   INTEGER NOT NULL,
 count     INTEGER NOT NULL,
 FOREIGN KEY(food_id) REFERENCES Food (id),
 FOREIGN KEY(user_id) REFERENCES User (id));

CREATE TABLE food_shop.Comment (
 id     INTEGER  PRIMARY KEY AUTO_INCREMENT,
 rate   INTEGER NOT NULL,
 text     TEXT);

CREATE TABLE food_shop.Order (
 id         INTEGER PRIMARY KEY AUTO_INCREMENT,
 user_id     INTEGER NOT NULL,
 shop_id     INTEGER NOT NULL,
 address_id  INTEGER NOT NULL,
 dis_id      INTEGER,
 comment_id  INTEGER, #nullable
 status      INTEGER NOT NULL,
 FOREIGN  KEY   (dis_id) REFERENCES Discount(id),
 FOREIGN  KEY   (address_id) REFERENCES Address(id),
 FOREIGN  KEY   (comment_id) REFERENCES Comment(id),
 FOREIGN  KEY   (shop_id) REFERENCES Shop(id),
 FOREIGN  KEY   (user_id) REFERENCES User(id));

CREATE TABLE food_shop.OrderFoodRelation (
 id         INTEGER PRIMARY KEY AUTO_INCREMENT,
 food_id    INTEGER NOT NULL,
 order_id   INTEGER NOT NULL,
 count      INTEGER NOT NULL,
 FOREIGN   KEY (order_id) REFERENCES food_shop.Order(id),
 FOREIGN   KEY (food_id) REFERENCES food_shop.Food(id));

#drop DATABASE food_shop;
#drop user food_shop_user;

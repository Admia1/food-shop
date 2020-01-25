#Database Fake Data feeler
INSERT INTO food_shop.City (name , geo_x, geo_y)
 VALUES ('Shiraz' , 300, 200);

INSERT INTO food_shop.City (name, geo_x, geo_y)
VALUES ('Tehran', 250, 1000);

INSERT INTO food_shop.City (name, geo_x, geo_y)
VALUES ('Esfehan', 200, 600);



INSERT INTO food_shop.User (first_name, last_name, password, email , phone_number)
VALUES ('mohsen', 'ziglari ' , 'zigil' , 'zigil@zigiloo.com' , '09171171717' );

INSERT INTO food_shop.User (first_name, last_name, password, email , phone_number)
VALUES ('mostafay', 'sa-adat ' , 'shalqam' , 'mostafa@yandex.com' , '0019324441122' );

INSERT INTO food_shop.User (first_name, last_name, password, email , phone_number)
VALUES ('rezvan ', 'zera-at ' , 'zanbor' , 'zard@honey.moon', '09882326261' );



INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('sare afif abad',             1,      302,   199,   1       );

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('vaast satarkhan' , 1, 301, 198,1);


INSERT INTO food_shop.Category (name)
VALUES ('kabab');

INSERT INTO food_shop.Category (name)
VALUES ('pizza');

INSERT INTO food_shop.Category (name)
VALUES ('potato');


INSERT INTO food_shop.Discount (code, percent)
VALUES ('YEK', 10);

INSERT INTO food_shop.Discount (code, percent)
VALUES ('DOU', 5);

INSERT INTO food_shop.Discount (code, percent)
VALUES ('SEH', 20);


INSERT INTO food_shop.Shop (city_id, name, min_bill_val, about, address_text, geo_x, geo_y)
VALUES (1, 'Kabab Kabab Shiraz' , 3500 , 'chelow kabab 3.5Tomani' , 'Khiaban saheli' , 300.5 , 200.4);

INSERT INTO food_shop.Shop (city_id, name, min_bill_val, about, address_text, geo_x, geo_y)
VALUES (1, 'Jigaraki naser',2000, ' jigarr makhsoos hazf pezeshki ','sar dozak', 299.8 , 194.4);

INSERT INTO food_shop.Shop (city_id, name, min_bill_val, about, address_text, geo_x, geo_y)
VALUES (1, 'sandevichi araba',5000, 'abdol kamal barat sandevich meyzane','mantaghe araba', 300.0 , 197.9);


INSERT INTO food_shop.DiscountUserRelation (dis_id, user_id)
VALUES (1, 1);

INSERT INTO food_shop.DiscountUserRelation (dis_id, user_id)
VALUES (2, 1);

INSERT INTO food_shop.DiscountUserRelation (dis_id, user_id)
VALUES (3, null);


INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (1, 3, 200 , 'poison kabab' , 0 , 'bokhori mordi' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (2, 2, 3000 ,'kabab khooboo', 0 , 'bokhori khordi' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (1, 3 , 5000 , 'Kotlet ' , 0.0 , 'Ali Zia\'s favorite food' );


INSERT INTO food_shop.FoodUserRelation (user_id, food_id, count)
VALUES (1, 2, 7);

INSERT INTO food_shop.FoodUserRelation (user_id, food_id, count)
VALUES (3, 1, 3);

INSERT INTO food_shop.FoodUserRelation (user_id, food_id, count)
VALUES (2, 1, 3);


INSERT INTO food_shop.Comment (text)
VALUES ('man too ghaza soosk didam');

INSERT INTO food_shop.Comment (text)
VALUES ('man too sooskam ghaza bood');

INSERT INTO food_shop.Comment (text)
VALUES ('ghaza mooyi mooyi bood');

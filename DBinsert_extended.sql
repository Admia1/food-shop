#Database Fake Data feeler
INSERT INTO food_shop.City (name , geo_x, geo_y)
 VALUES ('Shiraz' , 300, 200);

INSERT INTO food_shop.City (name, geo_x, geo_y)
VALUES ('Tehran', 250, 1000);

INSERT INTO food_shop.City (name, geo_x, geo_y)
VALUES ('Esfehan', 200, 600);

INSERT INTO food_shop.City (name , geo_x, geo_y)
VALUES ('Zarghoon' , 350, 230);

INSERT INTO food_shop.City (name , geo_x, geo_y)
VALUES ('Beyza' , 270, 160);

INSERT INTO food_shop.City (name, geo_x, geo_y)
VALUES ('Ghom', 430, 700);

INSERT INTO food_shop.City (name, geo_x, geo_y)
VALUES ('Jahrom', 500 , 700);

INSERT INTO food_shop.City (name, geo_x, geo_y)
VALUES ('Bandar Abas', 600, 700);




INSERT INTO food_shop.User (first_name, last_name, password, email , phone_number)
VALUES ('mohsen', 'ziglari ' , 'zigil' , 'zigil@zigiloo.com' , '09171171717' );

INSERT INTO food_shop.User (first_name, last_name, password, email , phone_number)
VALUES ('mostafay', 'sa-adat ' , 'shalqam' , 'mostafa@yandex.com' , '0019324441122' );

INSERT INTO food_shop.User (first_name, last_name, password, email , phone_number)
VALUES ('rezvan ', 'zera-at ' , 'zanbor' , 'zard@honey.moon', '09882326261' );

INSERT INTO food_shop.User (first_name, last_name, password, email , phone_number)
VALUES ('rezoy', 'edalat ' , 'justice' , 'edalat@justice.com' , '09362284591' );

INSERT INTO food_shop.User (first_name, last_name, password, email , phone_number)
VALUES ('ali', 'rahmani ' , 'holy' , 'rahmani@rahmani.com' , '09452547563' );

INSERT INTO food_shop.User (first_name, last_name, password, email , phone_number)
VALUES ('kazem', 'kazooyi' , 'squeerl' , 'kazoo@kazland.com' , '09414364535' );

INSERT INTO food_shop.User (first_name, last_name, password, email , phone_number)
VALUES ('jasem', 'naderi ' , 'password' , 'jas_43@yahoo.com' , '09179315725' );

INSERT INTO food_shop.User (first_name, last_name, password, email , phone_number)
VALUES ('mamad', 'bikar ' , 'incorrect' , 'mammad007@yahoo.com' , '09173620486' );

INSERT INTO food_shop.User (first_name, last_name, password, email , phone_number)
VALUES ('ali', 'aliyi ' , 'bruh' , 'alipunisher@yahoo.com' , '09175218604' );


INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('sare afif abad',             1,      302,   199,   1       );

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('vaast satarkhan' , 1, 301, 198, 1);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('avaloy sa-di' , 1, 305, 196, 1);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('avaloy sa-di kochey 7' , 1, 305, 196, 2);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('meydan etehad' , 1, 303, 198, 2);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('bolvar enghelab' , 2 , 600, 196, 3);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('meydan edalat' , 2 , 750 , 420 , 2);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('chara zendan' , 2, 541 , 720 , 2);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('adelabad' , 2, 750 , 420 , 2);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('zargari hamoo boridegi ke derakht dare ' , 1, 300 , 210 , 3);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('ma-ali abad khiaban doostan ' , 1, 290 , 410 , 3);


INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('ma-ali abad khiaban doostan ' , 1, 290 , 410 , 4);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('falkeye valfajr ' , 3, 290 , 410 , 4);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('meydoon ghasaba ' , 3, 320 , 400 , 4);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('chara zendan ' , 3, 330 , 450 , 4);

INSERT INTO food_shop.Address  (text, city_id, geo_x, geo_y, user_id)
VALUES ('falkeye valfajr ' , 4, 390 , 410 , 5);



INSERT INTO food_shop.Category (name)
VALUES ('kabab');

INSERT INTO food_shop.Category (name)
VALUES ('pizza');

INSERT INTO food_shop.Category (name)
VALUES ('potato');

INSERT INTO food_shop.Category (name)
VALUES ('salad');

INSERT INTO food_shop.Category (name)
VALUES ('breakfast');

INSERT INTO food_shop.Category (name)
VALUES ('dessert');

INSERT INTO food_shop.Category (name)
VALUES ('drink');

INSERT INTO food_shop.Category (name)
VALUES ('coffee');

INSERT INTO food_shop.Category (name)
VALUES ('hamburger');

INSERT INTO food_shop.Category (name)
VALUES ('chinese food');

INSERT INTO food_shop.Category (name)
VALUES ('italian');


INSERT INTO food_shop.Discount (code, percent)
VALUES ('YEK', 10);

INSERT INTO food_shop.Discount (code, percent)
VALUES ('DOU', 5);

INSERT INTO food_shop.Discount (code, percent)
VALUES ('SEH', 20);

INSERT INTO food_shop.Discount (code, percent)
VALUES ('FAJR', 20);

INSERT INTO food_shop.Discount (code, percent)
VALUES ('EYD', 20);

INSERT INTO food_shop.Discount (code, percent)
VALUES ('ASHOORA', 25);

INSERT INTO food_shop.Discount (code, percent)
VALUES ('VELADAT', 25);

INSERT INTO food_shop.Discount (code, percent)
VALUES ('ENGHELAB', 20);

INSERT INTO food_shop.Discount (code, percent)
VALUES ('CHRISTMAS', 30);


INSERT INTO food_shop.Shop (city_id, name, min_bill_val, about, address_text, geo_x, geo_y)
VALUES (1, 'Kabab Kabab Shiraz' , 3500 , 'chelow kabab 3.5Tomani' , 'Khiaban saheli' , 300.5 , 200.4);

INSERT INTO food_shop.Shop (city_id, name, min_bill_val, about, address_text, geo_x, geo_y)
VALUES (1, 'Jigaraki naser',2000, ' jigarr makhsoos hazf pezeshki ','sar dozak', 299.8 , 194.4);

INSERT INTO food_shop.Shop (city_id, name, min_bill_val, about, address_text, geo_x, geo_y)
VALUES (1, 'sandevichi araba',5000, 'abdol kamal barat sandevich meyzane','mantaghe araba', 300.0 , 197.9);

INSERT INTO food_shop.Shop (city_id, name, min_bill_val, about, address_text, geo_x, geo_y)
VALUES (1, 'Haft Khan',10000, 'yek zamani khoob bood','darvaze ghoran', 297.0 , 197.9);

INSERT INTO food_shop.Shop (city_id, name, min_bill_val, about, address_text, geo_x, geo_y)
VALUES (1, 'restooran ajdehaye sorkh ',10000, 'sells chinese food','park enghelab', 297.0 , 197.9);

INSERT INTO food_shop.Shop (city_id, name, min_bill_val, about, address_text, geo_x, geo_y)
VALUES (2, 'Khan Salar',10000, 'best mas moosir in whole country','darvaze ghoran', 360 , 230);

INSERT INTO food_shop.Shop (city_id, name, min_bill_val, about, address_text, geo_x, geo_y)
VALUES (2, 'coffee shop',15000, 'you know what people do in coffee shop ','a good place for not drinking coffee ', 297.0 , 197.9);

INSERT INTO food_shop.Shop (city_id, name, min_bill_val, about, address_text, geo_x, geo_y)
VALUES (1, 'coffee shop',15000, 'you know what people do in coffee shop ',' ma-ali abad', 297.0 , 197.9);


INSERT INTO food_shop.DiscountUserRelation (dis_id, user_id)
VALUES (1, 1);

INSERT INTO food_shop.DiscountUserRelation (dis_id, user_id)
VALUES (2, 1);

INSERT INTO food_shop.DiscountUserRelation (dis_id, user_id)
VALUES (3, null);

INSERT INTO food_shop.DiscountUserRelation (dis_id, user_id)
VALUES (4, null);

INSERT INTO food_shop.DiscountUserRelation (dis_id, user_id)
VALUES (5, null);

INSERT INTO food_shop.DiscountUserRelation (dis_id, user_id)
VALUES (6, null);

INSERT INTO food_shop.DiscountUserRelation (dis_id, user_id)
VALUES (7, null);

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (1, 3, 200 , 'poison kabab' , 0 , 'bokhori mordi' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (2, 2, 3000 ,'kabab khooboo', 0 , 'bokhori khordi' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (1, 3 , 5000 , 'Kotlet ' , 0.0 , 'Ali Zia\'s favorite food' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (1, 3, 200 , 'kabab bonab' , 0 , 'delicious and big' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (4, 4, 10000 , 'salad fasl' , 20 , 'best seasoning' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (4, 4, 13000 , 'salad ceasar' , 20 , 'he ate it when he was in Gaul' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (5, 5, 10000 , 'jello' , 10 , 'fruit jelly' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (4, 5, 12000 , 'jello' , 10 , 'fruit jelly' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (5, 5, 12000, 'panacota' , 10 , 'Dessert made in venice for queen of france' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (4, 5, 12000 , 'panacota' , 10 , 'Dessert made in venice for queen of france' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (4, 7, 15000 , 'latte' , 10 , ' First coffee in world that entered europe ' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (5, 7, 15000 , 'latte' , 10 , ' First coffee in world that entered europe ' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (6, 7, 15000 , 'latte' , 10 , ' First coffee in world that entered europe ' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (5, 9 , 15000 , 'nuddle' , 10 , ' delicuous chinese pork bon with nuddle' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (4, 7, 15000 , 'cappucino' , 10 , ' foam milk with enough sugar to keep you running' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (5, 7, 15000 , 'cappucino' , 10 , ' foam milk with enough sugar to keep you running' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (6, 7, 15000 , 'cappucino' , 10 , ' foam milk with enough sugar to keep you running' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (4, 7, 15000 , 'espresso' , 10 , ' 9 cups of coffee expressed in one ' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (5, 7, 15000 , 'espresso' , 10 , ' 9 cups of coffee expressed in one ' );

INSERT INTO food_shop.Food (shop_id, cat_id, price, name, discount , about)
VALUES (6, 7, 15000 , 'espresso' , 10 , ' 9 cups of coffee expressed in one ' );


INSERT INTO food_shop.FoodUserRelation (user_id, food_id, count)
VALUES (1, 2, 7);

INSERT INTO food_shop.FoodUserRelation (user_id, food_id, count)
VALUES (3, 1, 3);

INSERT INTO food_shop.FoodUserRelation (user_id, food_id, count)
VALUES (2, 1, 3);

-- 
-- INSERT INTO food_shop.Comment (text)
-- VALUES ('man too ghaza soosk didam');
--
-- INSERT INTO food_shop.Comment (text)
-- VALUES ('man too sooskam ghaza bood');
--
-- INSERT INTO food_shop.Comment (text)
-- VALUES ('ghaza mooyi mooyi bood');

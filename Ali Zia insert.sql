#Ali Zia Inserts
INSERT INTO food_shop.City (name , geo_x, geo_y)
 VALUES ('Shiraz' , 300, 200);



INSERT INTO kiho.User (firstname, lastname, password, email , phone)
VALUES ('aghoy ziglari', 'ziglari ' , 'zigil' , 'zigil@zigiloo.com' , '645636' );

INSERT INTO kiho.User (firstname, lastname, password, email , phone)
VALUES ('mostafay loolekesh', 'kazemi ' , 'loole' , 'mostafa@senfloolekesha.loole' , '1000016' );

INSERT INTO kiho.User (firstname, lastname, password, email , phone)
VALUES ('rezoy ', 'edalat ' , ' rez' , 'adalat@adoooo.com', '645636' );



INSERT INTO kiho.Address  (text, cityid, x, y, ownerid)
VALUES ('Khiaboon poshtoo. kochey baghali ', 1, 0, 0,1);

INSERT INTO kiho.Address  (text, cityid, x, y, ownerid)
VALUES ('Khiaboon enghelab. kochey baghali' , 1, 0, 0,1);

INSERT INTO kiho.Address  (text, cityid, x, y, ownerid)
VALUES ('Khiaboon satarkhan kochey baghali', 1, 0, 0,1);


INSERT INTO kiho.Category (name)
VALUES ('kabab');

INSERT INTO kiho.Category (name)
VALUES ('pizza');

INSERT INTO kiho.Category (name)
VALUES ('potato');

INSERT INTO kiho.Category (name)
VALUES ('peshkel');




INSERT INTO kiho.Discount (text, pencount)
VALUES ('Takhfifat tabestani!!!', 1);

INSERT INTO kiho.Discount (text, pencount)
VALUES ('Takhfifat Zemestani!!!', 5);

INSERT INTO kiho.Discount (text, pencount)
VALUES ('Takhfifat Arbain!!!', 1);


INSERT INTO kiho.Shop (cityid, name, min_bill_val, about, address_text, x, y)
VALUES (1, 'Kabab Kabab Shiraz' , 3500 , 'chelow kabab 3.5Tomani' , 'Khiaban saheli' , 5.0 , 6.0);

INSERT INTO kiho.Shop (cityid, name, min_bill_val, about, address_text, x, y)
VALUES (1, 'Jigaraki naser',2000, ' jigarr makhsoos hazf pezeshki ','sar dozak', 9.0 , 2.0);

INSERT INTO kiho.Shop (cityid, name, min_bill_val, about, address_text, x, y)
VALUES (1, 'sandevichi araba',5000, 'abdol kamal barat sandevich meyzane','mantaghe araba', 3.0 , 7.0);


INSERT INTO kiho.Access_Discount (dis_id, user_id)
VALUES (1, 1);

INSERT INTO kiho.Access_Discount (dis_id, user_id)
VALUES (2, 1);

INSERT INTO kiho.Access_Discount (dis_id, user_id)
VALUES (3, 2);


INSERT INTO kiho.Food (shopid, catid, price, name, discount ,percent , about)
VALUES (1, 3, 200 , 'poison kabab' , 0 ,0.0 , 'bokhori mordi' );

INSERT INTO kiho.Food (shopid, catid, price, name, discount , percent , about)
VALUES (2, 2, 3000 ,'kabab khooboo', 0 , 0.0 , 'bokhori khordi' );

INSERT INTO kiho.Food (shopid, catid, price, name, discount , percent , about)
VALUES (1, 3 , 5000 , 'Kotlet ', 0 , 0.0 , 'Ali Zia\'s favorite food' );


INSERT INTO kiho.GetinCart (userid, foodid, count)
VALUES (1, 2, 7);

INSERT INTO kiho.GetinCart (userid, foodid, count)
VALUES (3, 1, 3);

INSERT INTO kiho.GetinCart (userid, foodid, count)
VALUES (2, 1, 3);


INSERT INTO kiho.Comment (text)
VALUES ('man too ghaza soosk didam');

INSERT INTO kiho.Comment (text)
VALUES ('man too sooskam ghaza bood');

INSERT INTO kiho.Comment (text)
VALUES ('ghaza mooyi mooyi bood');

INSERT INTO kiho.Order (userid, shopid, addressid , disid, coomentid, status)
VALUES (1, 1, 4, 1,1,2);

INSERT INTO kiho.Order (userid, shopid, addressid, disid, coomentid, status)
VALUES (2, 3, 5, 3,2,2);

INSERT INTO kiho.Order (userid, shopid, addressid, disid, coomentid, status)
VALUES (1, 3, 6, 3,3,2);


INSERT INTO kiho.order_food_relation (foodid, orderid, count)
VALUES (1, 18, 3);

INSERT INTO kiho.order_food_relation (foodid, orderid, count)
VALUES (2, 19, 1);


INSERT INTO kiho.order_food_relation (foodid, orderid, count)
VALUES (3, 20, 1);
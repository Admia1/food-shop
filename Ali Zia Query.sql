#City

SELECT * FROM kiho.City WHERE ( id = ID );

SELECT * FROM kiho.City WHERE ( name = 'NAME' );

SELECT * FROM kiho.City WHERE ( location = 'LOCATION' );

SELECT * FROM kiho.City WHERE ( name = 'NAME' and location = 'LOCATION' );

INSERT INTO kiho.City ( name , location ) VALUES ('NAME' , 'LOCATION');

UPDATE kiho.City SET name = 'NAME' , location = 'LOCATION' WHERE id = ID;

#Address

SELECT * FROM kiho.Address WHERE ( id = ID );

SELECT * FROM kiho.Address WHERE ( text = 'TEXT' );

SELECT * FROM kiho.Address WHERE ( cityid = CITYID );

SELECT * FROM kiho.Address WHERE kiho.Address.cityid IN (SELECT id FROM kiho.City WHERE name = 'NAME'); # addresses in a specific city

SELECT * FROM kiho.Address WHERE ( ownerid = 'OWNERID' );

SELECT * FROM kiho.Address WHERE ( x < XU and x > XL and y<YU and y>YL); #give it double variables

SELECT * FROM kiho.Address WHERE kiho.Address.id IN (SELECT id FROM kiho.City); #this is useless to be honest

INSERT INTO kiho.Address ( text , cityid , x , y, ownerid )VALUES ('TEXT', CITYID , X , Y, OWNERID);

UPDATE kiho.Address SET text = 'TEXT' , cityid = CITYID , x = X , y = Y , ownerid  = OWNERID WHERE id = ID;

#Category

SELECT * FROM kiho.Category WHERE ( id = ID );

SELECT * FROM kiho.Category WHERE ( name = NAME);

INSERT INTO kiho.Category ( name )VALUES ('NAME');

UPDATE kiho.Category SET name = 'NAME' WHERE id = ID;

#User

SELECT * FROM kiho.User WHERE ( id = ID );

SELECT * FROM kiho.User WHERE ( firstname = 'FIRSTNAME' );

SELECT * FROM kiho.User WHERE ( email = 'EMAIL' );

SELECT * FROM kiho.User WHERE ( email = 'EMAIL' and password = 'PASSWORD' );

INSERT INTO kiho.User ( firstname , lastname , password , email , phone )
		VALUES ('FIRSTNAME' , 'LASTNAME' , 'PASSWORD' , 'EMAIL' , 'PHONE' );

UPDATE kiho.User SET firstname = 'FIRSTNAME' , lastname = 'LASTNAME' , password = 'PASSWORD' , email = 'EMAIL' , phone = 'PHONE' WHERE id = ID;

#Discount

SELECT * FROM kiho.Discount WHERE ( id = ID );

INSERT INTO kiho.Discount ( text , pencount ) VALUES ('TEXT' , PENCOUNT);

UPDATE kiho.Discount SET text = 'TEXT' , pencount = PENCOUNT WHERE id = ID;

#Shop

SELECT * FROM kiho.Shop WHERE ( id = ID );

SELECT * FROM kiho.Shop WHERE ( cityid = CITYID );

SELECT * FROM kiho.Shop WHERE kiho.Shop.cityid IN (SELECT id FROM kiho.City WHERE name = 'NAME'); #shops in a specific city

SELECT * FROM kiho.Shop WHERE ( min_bill_val < MINBILL );

SELECT * FROM kiho.Shop WHERE ( min_bill_val < MINBILL and cityid = CITYID );

SELECT * FROM kiho.Shop WHERE ( x < XU and x > XL and y<YU and y>YL );

INSERT INTO kiho.Shop (cityid, name, min_bill_val, about, address_text, x, y)
VALUES (CITYID, 'NAME',MINBILL, 'ABOUT','ADDRESS', X , Y);

UPDATE kiho.Shop SET cityid = CITYID , name = 'NAME', min_bill_val = MINBILL , about = 'ABOUT' , address_text = 'ADDRESS' , x= X , y = Y WHERE id = ID;

#Access_Discount

SELECT * FROM kiho.Access_Discount ;

SELECT * FROM kiho.Access_Discount WHERE ( dis_id = DISID );

SELECT * FROM kiho.Access_Discount WHERE ( user_id = USERID );

SELECT * FROM kiho.Access_Discount WHERE ( user_id = USERID and dis_id = DISID);

INSERT INTO kiho.Access_Discount ( dis_id , user_id ) VALUES ( DISID , USERID );

UPDATE kiho.Access_Discount SET dis_id = DISID , user_id = USERID WHERE id = ID;

#Food

SELECT * FROM kiho.Food

SELECT * FROM kiho.Food WHERE ( dis_id = DISID );

SELECT * FROM kiho.Food WHERE ( shopid = SHOPID);

SELECT * FROM kiho.Food WHERE ( catid = CATID);

SELECT * FROM kiho.Food WHERE ( shopid = SHOPID and catid = CATID);

INSERT INTO kiho.Food (shopid, catid , price, name, discount ,percent , about)
VALUES (SHOPID, CATID , PRICE , 'NAME' , DISCOUNT , PERCENT , 'ABOUT' );

UPDATE kiho.Food SET shopid = SHOPID , catid = CATID , price = PRICE , name = 'NAME' , discount = DISCOUNT , percent = PERCENT , about = 'ABOUT' WHERE id = ID;

#GetinCart

SELECT * FROM kiho.GetinCart;

SELECT * FROM kiho.GetinCart WHERE (id = ID);

SELECT * FROM kiho.GetinCart WHERE (userid = USERID);

SELECT * FROM kiho.GetinCart WHERE (foodid = FOODID);

INSERT INTO kiho.GetinCart (userid, foodid , count) VALUES (USERID,FOODID,COUNT);

UPDATE kiho.GetinCart SET userid = USERID , foodid = FOODID , count = COUNT WHERE id = ID;


#Comment

SELECT * FROM kiho.Comment WHERE (id = ID);

INSERT INTO kiho.Comment ( text) VALUES ('TEXT');

#Order

SELECT * FROM kiho.Order WHERE (id = ID);

SELECT * FROM kiho.Order WHERE (userid = USERID);

SELECT * FROM kiho.Order WHERE (shopid = SHOPID);

SELECT * FROM kiho.Order WHERE ((userid = USERID and shopid = SHOPID);

SELECT * FROM kiho.Order JOIN kiho.Comment on kiho.Order.coomentid = kiho.Comment.id #order with comment

INSERT INTO kiho.Order (userid, shopid, addressid, disid, coomentid, status)
VALUES (USERID, SHOPID, ADDRESSID, DISID , COMID , STATUS);

UPDATE kiho.Order SET userid = USERID , shopid = SHOPID , addressid = ADDRESSID , disid= DISID , coomentid = COOMENTID , status = STATUS WHERE id = ID;

#order_food_relation

SELECT * FROM kiho.order_food_relation;

SELECT * FROM kiho.order_food_relation WHERE (id = ID);

SELECT * FROM kiho.order_food_relation WHERE (orderid = ORDERID);

INSERT INTO kiho.order_food_relation (foodid, orderid, count)
VALUES (FOODID, ORDERID , COUNT );

UPDATE kiho.order_food_relation SET foodid = FOODID , orderid = ORDERID , count = COUNT WHERE id = ID;

#special purpose

SELECT * FROM kiho.Food JOIN kiho.Shop on kiho.Food.shopid = kiho.Shop.id join kiho.Category on kiho.Food.catid=kiho.Category.id

Select kiho.GetinCart.id , kiho.GetinCart.count , kiho.Food.name , kiho.Food.discount , kiho.Food.percent ,kiho.Food.price from kiho.GetinCart left outer join kiho.Food on (kiho.GetinCart.foodid = kiho.Food.id) WHERE kiho.GetinCart.userid = ID;

Select

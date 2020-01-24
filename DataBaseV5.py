import mysql.connector as mariadb

try:
    mariadb_connection = mariadb.connect(user='kiho', password='kiho', database='kiho')
except:
    print("oh fuck")
cursor = mariadb_connection.cursor()

def print_list(result):
        for row in result:
            for col in row:
                print(col)
def Select_Cities():
        cursor.execute("SELECT * FROM City")
        result = cursor.fetchall()
        return result
def Select_Cities_by_ID(ID):#give it int
        cursor.execute("SELECT * FROM City WHERE id = "+str(ID))
        result = cursor.fetchall()
        return result        
def Select_Cities_by_name(NAME):#give it str
        cursor.execute("SELECT * FROM City WHERE name = '"+ NAME +"'")
        result = cursor.fetchall()
        return result
def Insert_Into_City(NAME,LOCATION):
    cursor.execute("INSERT INTO City ( name , location ) VALUES ('"+NAME+"' , '"+LOCATION+"');")
    return
def Update_City(ID,NAME,LOCATION):
    cursor.execute("UPDATE City SET name = '"+NAME+"' , location = '"+LOCATION+"' WHERE id = "+str(ID)+";")
def Select_Address():
    cursor.execute("SELECT * FROM Address;")
    result = cursor.fetchall()
    return result
def Select_Address_by_ID(ID):
    cursor.execute("SELECT * FROM Address WHERE ( id = "+str(ID)+" );")
    result = cursor.fetchall()
    return result
def Select_Address_by_CityID(CITYID):
    cursor.execute("SELECT * FROM Address WHERE ( cityid = "+str(CITYID)+" );")
    result = cursor.fetchall()
    return result
def Select_Address_by_City_name(NAME):
    cursor.execute("SELECT * FROM Address WHERE Address.cityid IN (SELECT id FROM City WHERE name = '"+NAME+"');")
    result = cursor.fetchall()
    return result
def Select_Address_by_OwnerID(OWNERID):
    cursor.execute("SELECT * FROM Address WHERE ( ownerid = "+OWNERID+";")
    result = cursor.fetchall()
    return result
def Select_Address_by_Range(XL,XU,YL,YU): #give these as double, X lower, X upper, Y lower, Y upper
    cursor.execute("SELECT * FROM Address WHERE ( x < "+str(XU)+" and x > "+str(XL)+" and y<"+str(YU)+" and y>"+str(YL)+"); ")
    result = cursor.fetchall()
    return result
def Insert_Into_Address(TEXT , CITYID , X , Y , OWNERID):
    cursor.execute("INSERT INTO Address ( text , cityid , x , y, ownerid )VALUES ('"+TEXT+"', "+str(CITYID)+" , "+str(X)+" , "+str(Y)+", "+str(OWNERID)+");")
    return
def Update_Address():
    cursor.execute("UPDATE Address SET text = '"+TEXT+"' , cityid = +"str(CITYID)+" , x = "+str(X)+" , y = "+str(Y)+" , ownerid  = "+str(OWNERID)+" WHERE id = "str(ID)";")
    return
def Select_Category():
    cursor.execute("SELECT * FROM Category ")
    result = cursor.fetchall()
    return result
def Select_Category_by_ID(ID):
    cursor.execute("SELECT * FROM Category WHERE ( id = "+str(ID)+" )")
    result = cursor.fetchall()
    return result
def Select_Category_by_name(NAME):#give it str
        cursor.execute("SELECT * FROM Category WHERE ( name = '"+ NAME +"'")
        result = cursor.fetchall()
        return result
def Insert_Into_Category(NAME):
    cursor.execute("INSERT INTO Category ( name )VALUES ('"+NAME+"');")
    return
def Update_Category(ID , Name):
    cursor.execute("UPDATE Category SET name = '"+NAME+"' WHERE id = "+str(ID)+";")
    return
def Select_User():
    cursor.execute("SELECT * FROM User")
    result = cursor.fetchall()
    return result
def Select_User_by_ID(ID):
    cursor.execute("SELECT * FROM User WHERE ( id = "+str(ID)+" );")
    result = cursor.fetchall()
    return result
def Select_User_by_Name(FIRSTNAME):
    cursor.execute("SELECT * FROM User WHERE ( firstname = '"+FIRSTNAME+"' );")
    result = cursor.fetchall()
    return result
def Select_User_by_Email(EMAIL):
    cursor.execute("SELECT * FROM User WHERE ( email = '"+EMAIL+"' );")
    result = cursor.fetchall()
    return result
def Select_User_by_Email_and_Pass(EMAIL , PASSWORD): #for login
    cursor.execute("SELECT * FROM User WHERE ( email = '"+EMAIL+"' and password = '"+PASSWORD+"' );")
    result = cursor.fetchall()
    return result
def Insert_Into_User(FIRSTNAME , LASTNAME , PASSWORD , EMAIL , PHONE):
    cursor.execute("INSERT INTO User ( firstname , lastname , password , email , phone )
VALUES ('"+FIRSTNAME+"' , '"+LASTNAME+"' , '"+PASSWORD+"' , '"+EMAIL+"' , '"+PHONE+"' );")
    return
def Update_User(FIRSTNAME,LASTNAME,PASSWORD,EMAIL,PHONE,ID):
    cursor.execute("UPDATE User SET firstname = '"+FIRSTNAME+"' , lastname = '"+LASTNAME+"' , password = '"+PASSWORD+"' , email = '"+EMAIL+"' , phone = '"+PHONE+"' WHERE id = "+str(ID)+";")
    return
def Select_Discount():
    cursor.execute("SELECT * FROM Discount")
    result = cursor.fetchall()
    return result
def Select_Discount_by_ID(ID):
    cursor.execute("SELECT * FROM Discount WHERE ( id = "+str(ID)+" );")
    result = cursor.fetchall()
    return result
def Insert_Into_Discount():
    cursor.execute("INSERT INTO Discount ( text , pencount ) VALUES ('"+TEXT+"' , "+str(PENCOUNT)+" ;")
    return
def Update_Discount():
    cursor.execute("UPDATE Discount SET text = '"+TEXT+"' , pencount = "+str(PENCOUNT)+" WHERE id = "+str(ID)+" ;")
    return
def Select_Food():
    cursor.execute("SELECT * FROM Food")
    result = cursor.fetchall()
    return result
def Select_Food_by_DISID(DISID):
    cursor.execute("SELECT * FROM Food WHERE ( dis_id = "+str(DISID)+" );")
    result = cursor.fetchall()
    return result
def Select_Food_by_SHOPID(SHOPID):
    cursor.execute("SELECT * FROM Food WHERE ( shopid = "+str(SHOPID)+")")
    result = cursor.fetchall()
    return result
def Select_Food_by_CATID(CATID):
    cursor.execute("SELECT * FROM Food WHERE ( catid = "+str(CATID)+");")
    result = cursor.fetchall()
    return result
def Select_Food_by_Shop_and_Cat(SHOPID , CATID):
    cursor.execute("SELECT * FROM Food WHERE ( shopid = "+str(SHOPID)+" and catid = "+str(CATID)+");")
    result = cursor.fetchall()
    return result
def Insert_Into_Food(SHOPID , CATID , NAME , DISCOUNT , PERCENT , ABOUT):
    cursor.execute("INSERT INTO Food (shopid, catid , price, name, discount ,percent , about)
VALUES ("+str(SHOPID)+", "+str(CATID)+" , "+str(PRICE)+" , '"+NAME+"' , "+str(DISCOUNT)+" , "+str(PERCENT)+" , '"+ABOUT+"' );")
def Update_Food(SHOPID , CATID):
    cursor.execute("UPDATE Food SET shopid = "+str(SHOPID)+" , catid = "+str(CATID)+" , price = "+str(PRICE)+" , name = '"+NAME+"' , discount = "+str(DISCOUNT)+" , percent = "+str(PERCENT)+" , about = '"+ABOUT+"' WHERE id = "+str(ID)+";")
    return
def Select_GetinCart():
    cursor.execute("SELECT * FROM GetinCart;")
    result = cursor.fetchall()
    return result
def Select_GetinCart_by_ID(ID):
    cursor.execute("SELECT * FROM GetinCart WHERE (id = "+str(ID)+");")
    result = cursor.fetchall()
    return result
def Select_GetinCart_by_ID(USERID):
    cursor.execute("SELECT * FROM GetinCart WHERE (userid = "+str(USERID)+");")
    result = cursor.fetchall()
    return result
def Insert_Into_GetinCart(USERID , FOODID , COUNT):
    cursor.execute("INSERT INTO GetinCart (userid, foodid , count) VALUES ("+str(USERID)+" , "+str(FOODID)+","+str(COUNT)+");")
    return
def Update_GetinCart(USERID , FOODID , COUNT , ID):
    cursor.execute("UPDATE GetinCart SET userid = "+str(USERID)+" , foodid = "+str(FOODID)+" , count = "+str(COUNT)+" WHERE id = "+str(ID)+";")

def Select_Comment_by_ID(ID):
    cursor.execute("SELECT * FROM Comment WHERE (id = "+str(ID)+");")
    result = cursor.fetchall()
    return result
def Insert_Into_Comment(TEXT):
    cursor.execute("INSERT INTO Comment ( text) VALUES ('"+TEXT+"');")
    return
def Update_Comment(TEXT,ID):
    cursor.execute("UPDATE Comment SET text = '"+TEXT+"' WHERE id = "+str(ID)+";")
    return
def Select_Order():
    cursor.execute("SELECT * FROM Order;")
    result = cursor.fetchall()
    return result
def Select_Order_by_ID(ID):
    cursor.execute("SELECT * FROM Order WHERE id = "+str(ID)+" ; ")
    result = cursor.fetchall()
    return result
def Select_Order_by_USERID(USERID):
    cursor.execute("SELECT * FROM Order WHERE (userid = "+str(USERID)+"); ")
    result = cursor.fetchall()
    return result
def Select_Order_by_SHOPID(SHOPID):
    cursor.execute("SELECT * FROM Order WHERE (shopid = "+str(SHOPID)+");")
    result = cursor.fetchall()
    return result
def Select_Order_With_Comment():
    cursor.execute("SELECT * FROM Order JOIN Comment on Order.coomentid = Comment.id ")
    result = cursor.fetchall()
    return result
def Insert_Into_Order(USERID , SHOPID , ADDRESSID , DISID , COMID , STATUS):
    cursor.execute("INSERT INTO Order (userid, shopid, addressid, disid, coomentid, status)
VALUES ("+str(USERID)+", "+str(SHOPID)+", "+str(ADDRESSID)+", "+str(DISID)+" , "+str(COMID)+" , "+str(STATUS)+"); ")
def Update_Order(USERID , SHOPID , ADDRESSID , DISID , COOMENTID , STATUS , ID):
    cursor.execute("UPDATE Order SET userid = "+str(USERID)+" , shopid = "+str(SHOPID)+" , addressid = "+str(ADDRESSID)+" , disid= "+str(DISID)+" , coomentid = "+str(COOMENTID)+" , status = "+str(STATUS)+" WHERE id = "+str(ID)+";
")
    return
def Update_Order_Comment_Only(COOMENTID , ID):
    cursor.execute("UPDATE Order SET  coomentid = "+str(COOMENTID)+"  WHERE id = "+str(ID)+";
")
    
def Select_Order_Food_Relation():
    cursor.execute("SELECT * FROM order_food_relation; ")
    result = cursor.fetchall()
    return result
def Select_Order_Food_Relation_by_ID(ID):
    cursor.execute("SELECT * FROM order_food_relation WHERE (id = "+str(ID)+");")
    result = cursor.fetchall()
    return result
def Select_Order_Food_Relation_by_OrderID(ORDERID):
    cursor.execute("SELECT * FROM order_food_relation WHERE (orderid = "+str(ORDERID)+");")
    result = cursor.fetchall()
    return result
def Insert_Into_Order_Food_Relation(FOODID , ORDERID , COUNT):
    cursor.execute("INSERT INTO order_food_relation (foodid, orderid, count)
VALUES ("+str(FOODID)+", "+str(ORDERID)+" , "+str(COUNT)+" );")
    return
def Update_Order_Food_Relation(FOODID , ORDERID , COUNT , ID):
    cursor.execute("UPDATE order_food_relation SET foodid = "+str(FOODID)+" , orderid = "+str(ORDERID)+" , count = "+str(COUNT)+" WHERE id = "+str(ID)+";")


def Select_Food_of_every_shop(SHOPID):  #catalog of that shop
    cursor.execute("SELECT * FROM Food JOIN Shop on Food.shopid = Shop.id join Category on Food.catid=Category.id WHERE Food.shopid = "+str(SHOPID)+";")
    result = cursor.fetchall()
    return result

    





def Select_on_going_purchase(int user_id):
    cursor.execute("Select GetinCart.id , GetinCart.count , Food.name , Food.discount , Food.percent ,Food.price from GetinCart left outer join Food on (GetinCart.foodid = Food.id) WHERE GetinCart.userid = "+str(ID)+";")
    result = cursor.fetchall()
    return result


result = Select_Cities()
print_list(result)
result = Select_Cities_by_ID(4)
print_list(result)
result = Select_Cities_by_name("shiraz")
print_list(result)
Insert_Into_City("jasem","ghasem")

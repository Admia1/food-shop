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

result = Select_Cities()
print_list(result)
result = Select_Cities_by_ID(4)
print_list(result)
result = Select_Cities_by_name("shiraz")
print_list(result)
Insert_Into_City("jasem","ghasem")

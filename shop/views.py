from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from random import randint

import mysql.connector as mariadb
mariadb_connection = mariadb.connect(user='food_shop_user', password='food_shop_user_password', database='food_shop')
cursor = mariadb_connection.cursor()

active_cookies = {}#key user_id
db_users = []
db_cities = [{'id':1, 'name':'Shiraz'}, {'id':2, 'name':'Tehran'}, {'id':3, 'name':'Isfehan'}, {'id':4, 'name':'Mash-had'}]

db_shops  = [{'id':2, 'name':'pam-chal', 'about':'no about', 'city_id':1, 'mbv':3000, 'x':100, 'y':100, 'address_text':'end of Afif Abad'},
          {'id':3, 'name':'Namak', 'about':'no about', 'city_id':1, 'mbv':13000, 'x':99, 'y':100, 'address_text':'middle of Afif Abad'},
          {'id':4, 'name':'Narvan', 'about':'no about', 'city_id':1, 'mbv':15000, 'x':101, 'y':100, 'address_text':'end of Afif Abad'},
          {'id':5, 'name':'pam-chal Tehran', 'about':'no about', 'city_id':2, 'mbv':3000, 'x':1000, 'y':2000, 'address_text':'Afif Abad of Tehran'},
          {'id':6, 'name':'pam-chal Isfehan', 'about':'no about', 'city_id':3, 'mbv':5000, 'x':2000, 'y':3000, 'address_text':'Afif Abad of Isfehan'},
          {'id':7, 'name':'pam-chal Mash-had', 'about':'no about', 'city_id':4, 'mbv':2000, 'x':-1000, 'y':5000, 'address_text':'Afif Abad of Mash-had'},
        ]
db_foods  = [{'id':2, 'name':'pizza', 'price':20000, 'discounted_price':19000, 'discount':30, 'about':'circle food', 'shop_id':1, 'cat_id':4},
          {'id':3, 'name':'burger', 'price':21000, 'discounted_price':15500, 'discount':30, 'about':'made by sponge bob', 'shop_id':1, 'cat_id':2},
          {'id':4, 'name':'chips', 'price':22000, 'discounted_price':14000, 'discount':30, 'about':'circle food', 'shop_id':1, 'cat_id':3},
          {'id':5, 'name':'veg pizza', 'price':23000, 'discounted_price':21500, 'discount':30, 'about':'circle food', 'shop_id':1, 'cat_id':4},
          {'id':6, 'name':'pasta', 'price':24000, 'discounted_price':19200, 'discount':30, 'about':'circle food', 'shop_id':1, 'cat_id':4},
          {'id':7, 'name':'meat pizza', 'price':25000, 'discounted_price':19000, 'discount':30, 'about':'circle food', 'shop_id':1, 'cat_id':4},
          {'id':8, 'name':'chips', 'price':26000, 'discounted_price':19300, 'discount':30, 'about':'my favorite', 'shop_id':2, 'cat_id':3},
          {'id':9, 'name':'soup', 'price':27000, 'discounted_price':24300, 'discount':30, 'about':'in a bowl', 'shop_id':2, 'cat_id':5},
          {'id':10, 'name':'chese burger', 'price':28000, 'discounted_price':27000, 'discount':32, 'about':'made by sponge bob', 'shop_id':3, 'cat_id':2},
          {'id':11, 'name':'mushroom burger', 'price':29000, 'discounted_price':19000, 'discount':34, 'about':'circle food', 'shop_id':3, 'cat_id':2},
          {'id':12, 'name':'pizza', 'price':11000, 'discounted_price':9000, 'discount':30, 'about':'circle food', 'shop_id':4, 'cat_id':4},
          {'id':13, 'name':'hotdog of Tehran', 'price':12000, 'discounted_price':8000, 'discount':30, 'about':'long long away', 'shop_id':5, 'cat_id':1},
          {'id':14, 'name':'hotdog of Isfehan', 'price':14000, 'discounted_price':9500, 'discount':15, 'about':'long long away', 'shop_id':6, 'cat_id':1},
          {'id':15, 'name':'hotdog of Mash-had', 'price':15000, 'discounted_price':1400, 'discount':10, 'about':'long long away', 'shop_id':7, 'cat_id':1},
        ]
db_cat = [{'id':1, 'name':'hotdog'},
       {'id':2, 'name':'burger'},
       {'id':3, 'name':'potato'},
       {'id':4, 'name':'pizza'},
       {'id':5, 'name':'soup'}
    ]
db_discounts = [{'id':1,'code':'xalix', 'percent':10}] #{'id':2,'code':'xalix', 'percent':10}
db_discount_user_relation = [{'id':1, 'user_id':0, 'discount_id':1}] #{'id':1, 'user_id':1(0 for all), 'discount_id':1}
db_addresses = [] #{'id':1,'text':'here', 'city_id':1,'user_id':1, 'x':30, 'y':50}
db_comments = []
db_orders = []
db_order_food_relation = []#{'id':1 , 'food_id':12, 'order_id':2, 'count':3}
db_got_in_chart = []


def add_cookie(user_id):
    new_cookie = randint(100000000000000000000000,100000000000000000000000*10-1)
    while(new_cookie in active_cookies):
        new_cookie = randint(100000000000000000000000,100000000000000000000000*10-1)
    active_cookies.update({str(new_cookie): user_id})
    print(active_cookies)
    return new_cookie

def post_validator(request, field):
    if field not in request.POST:
        return False
    if not request.POST[field]:
        return False
    return True

def register(request):
    if 'food-shop-cookie' in request.COOKIES:
        if active_cookies.get(request.COOKIES['food-shop-cookie']):
            return HttpResponseRedirect(reverse('shop:dashboard'))

    template='shop/register.html'
    if not request.method == 'POST':
        return render(request, template, {})


    #do sth with request.POST['KEY']
    for field in ['first_name', 'last_name', 'password', 'confirm_password', 'email', 'phone_number']:
        if not post_validator(request,field):
            return render(request, template, {'error_message' : 'invalid post form : '+field})

    for charr in request.POST['phone_number']:
        if charr not in "1234567890" :
            return render(request, template, {'error_message' : 'invalid post : phone_number must be integer'})

    if request.POST['password'] != request.POST['confirm_password']:
        return render(request, template, {'error_message' : 'invalid post : password and confirm_password must be the same'})

    #to do email validator
    #to do name validator
    #to do phone number validator
    #to do password
    cursor.execute(f"select * from User where email ='{request.POST['email']}'")
    res = cursor.fetchall()
    if res:
        return render(request, template, {'error_message' : 'invalid post : you registered before'})
    cursor.execute(f"INSERT INTO User (first_name, last_name, password, email , phone_number) VALUES ('" +request.POST['first_name']+"' , '"+request.POST['last_name']+"' , '"+request.POST['password']+"' , '"+request.POST['email']+"' , '"+request.POST['phone_number']+"' )")
    cursor.execute(f"select * from User where email='{request.POST['email']}'")
    new_user_id = cursor.fetchall()[0][0]
    t = loader.get_template('shop/login.html')
    content = {'logged_in': True, 'error_message':'you logged in'}
    response = HttpResponse(t.render(content, request))
    new_cookie = add_cookie(new_user_id)
    response.set_cookie('food-shop-cookie',str(new_cookie))

    return response


def login(request):
    print(db_users)
    if 'food-shop-cookie' in request.COOKIES:
        print(request.COOKIES['food-shop-cookie'])
        if active_cookies.get(request.COOKIES['food-shop-cookie']):
            return HttpResponseRedirect(reverse('shop:dashboard'))

    template='shop/login.html'
    if request.method != 'POST':
        return render(request, template, {})
    if ('email' not in request.POST) or ('password' not in request.POST):
        return render(request, template, {'error_message' : "bad post format", 'logged_in' : False})

    cursor.execute(f"select * from User where email='{request.POST['email']}' and password='{request.POST['password']}'")
    res= cursor.fetchall()
    if not res:
        return render(request, template, {'error_message' : "Wrong email or password", 'logged_in' : False})
    cur_user_id = res[0][0]
    t = loader.get_template('shop/login.html')
    content = {'logged_in': True, 'error_message':'you logged in'}
    response = HttpResponse(t.render(content, request))
    new_cookie = add_cookie(cur_user_id)
    response.set_cookie('food-shop-cookie',str(new_cookie))

    return response

def logout(request):
    if 'food-shop-cookie' in request.COOKIES:
        if active_cookies.get(request.COOKIES['food-shop-cookie']):
            active_cookies.pop(request.COOKIES['food-shop-cookie'])

    return HttpResponseRedirect(reverse('shop:login'))

def profile(request):
    template = 'shop/profile.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    cursor.execute(f"select * from User where User.id={cur_user_id}")
    data = cursor.fetchone()
    cur_user= {'id':data[0], 'first_name':data[1], 'last_name':data[2], 'email':data[4], 'phone_number':data[5]}
    if request.method!='POST':
        return render(request, template, {'user':cur_user})

    for field in ['first_name', 'last_name', 'phone_number']:
        if not post_validator(request,field):
            return render(request, template, {'error_message' : 'invalid post form : '+field, 'user':cur_user})

    for charr in request.POST['phone_number']:
        if charr not in '1234567890':
            return render(request, template, {'error_message' : 'invalid phone_number' , 'user':cur_user})

    cursor.execute(f"UPDATE User SET first_name = '{request.POST['first_name']}' , last_name = '{request.POST['last_name']}' , phone_number = '{request.POST['phone_number']}' WHERE id = {cur_user_id}")


    cursor.execute(f"select * from User where User.id={cur_user_id}")
    data = cursor.fetchone()
    cur_user= {'id':data[0], 'first_name':data[1], 'last_name':data[2], 'email':data[4], 'phone_number':data[5]}
    return HttpResponseRedirect(reverse("shop:profile"))
    #return render(request, template, {'user':cur_user})


def dashboard(request):
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    template='shop/dashboard.html'
    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])

    cursor.execute(f"select * from User where User.id={cur_user_id}")
    data = cursor.fetchone()
    cur_user= {'id':data[0], 'first_name':data[1], 'last_name':data[2], 'email':data[4], 'phone_number':data[5]}
    return render(request, template, {'cities':db_cities, 'user':cur_user})


def shops_city(request, city_id):

    cursor.execute(f"select * from City where id={city_id}")
    res = cursor.fetchall()
    if not res:
        return render(request, 'shop/shops.html', {'error_message':'invalid city id'})

    cursor.execute(f"select * from Shop where city_id={city_id}")
    city = {'name' : res[0][1]}

    data = cursor.fetchall()
    shops = [{'id':dat[0], 'name':dat[2]}for dat in data]

    return render(request, 'shop/shops.html', {'city':city, 'shops':shops})

def shops_location(request):
    if (request.method != 'POST') or ('geo_x' not in request.POST) or ('geo_y' not in request.POST):
        return render(request, 'shop/shops.html', {'error_message':'invalid post format'})
    try:
        geo_x = float(request.POST['geo_x'])
        geo_y = float(request.POST['geo_y'])
    except:
        return render(request, 'shop/shops.html', {'error_message':'invalid format geo_x geo_y'})

    near_shops=[]
    for shop in db_shops:
        if ( (shop['x']-geo_x)**2 + (shop['y']-geo_y)**2 ) <= 50*2:
            near_shops.append(shop)
    return render(request, 'shop/shops.html', {'shops':near_shops})

def shop(request, shop_id):
    template = 'shop/shop.html'

    cursor.execute(f"select * from Shop where id={shop_id}")
    res = cursor.fetchall()
    if not res:
        return render(request, template, {'error_message':'wrong shop id'})

    cursor.execute(f"select * from Food where shop_id={shop_id}")
    data = cursor.fetchall()
    cur_shop = {'name':res[0][2], 'id':res[0][0]}
    foods=[{'name':dat[4], 'price':dat[3], 'discounted_price':dat[3]*(100-dat[5])/100, 'id':dat[0]} for dat in data]
    if request.method != 'POST':
        return render(request, template, {'shop':cur_shop, 'foods':foods})
    #add or remove item
    #TODO dont buy from 2 shops
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    cursor.execute(f"select * from User where User.id={cur_user_id}")
    data = cursor.fetchone()
    cur_user= {'id':data[0], 'first_name':data[1], 'last_name':data[2], 'email':data[4], 'phone_number':data[5]}
    for field in ['food_id', 'count']:
        if not post_validator(request,field):
            return render(request, template, {'error_message' : 'invalid post form : '+field, 'shop':cur_shop, 'foods' : foods})
    try:
        food_id = int(request.POST['food_id'])
        count = int(request.POST['count'])
        if count not in [1,-1]:
            raise 1
    except:
        return render(request, template, {'error_message':'geo_x geo_y bad format', 'shop':cur_shop, 'foods':foods})

    cursor.execute(f"select * from FoodUserRelation where food_id={food_id} and user_id={str(cur_user_id)}")
    res = cursor.fetchall()

    if not res:
        if count == 1:
            cursor.execute(f"INSERT INTO FoodUserRelation ( user_id , food_id , count)VALUES ({cur_user_id},{food_id},1)")
        else:
            return render(request, template, {'error_message':'nothing to remove', 'shop':cur_shop,'foods':foods})
    else:
        cur_count = res[0][3]
        cur_count += count
        if cur_count == 0:
            cursor.execute(f"delete from FoodUserRelation WHERE id = {res[0][0]}")
        else:
            cursor.execute(f"UPDATE FoodUserRelation SET count = {cur_count} WHERE id = {res[0][0]}")

    return render(request, template, {'shop':cur_shop, 'foods':foods})


def addresses(request):
    template = 'shop/addresses.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    cursor.execute(f"select * from User where User.id={cur_user_id}")
    data = cursor.fetchone()
    cur_user= {'id':data[0], 'first_name':data[1], 'last_name':data[2], 'email':data[4], 'phone_number':data[5]}

    cursor.execute(f"select * from Address where user_id={cur_user_id}")
    data = cursor.fetchall()
    user_addresses = [{'id':dat[0], 'text':dat[1], 'city_id':dat[2], 'user_id':dat[3], 'geo_x':dat[4], 'geo_y':dat[5]}for dat in data]
    if request.method != "POST":
        return render(request, template, {'addresses':user_addresses})


    for field in ['city_id', 'text', 'geo_x', 'geo_y']:
        if not post_validator(request,field):
            return render(request, template, {'error_message' : 'invalid post form : '+field, 'addresses':user_addresses})
    try:
        geo_x=float(request.POST['geo_x'])
        geo_y=float(request.POST['geo_y'])
    except:
        return render(request, template, {'error_message':'geo_x geo_y bad format'})

    cursor.execute(f"INSERT INTO Address ( text , city_id , geo_x , geo_y, user_id )VALUES ('{request.POST['text']}',{request.POST['city_id']},{request.POST['geo_x']} ,{request.POST['geo_y']},{cur_user_id})")
    return HttpResponseRedirect(reverse('shop:addresses'))


def address(request, address_id):
    template = 'shop/address.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])

    cursor.execute(f"select * from Address where user_id={cur_user_id} and id={address_id}")
    data = cursor.fetchall()
    if not data:
        return render(request, template, {'error_message':'wrong address id'})
    data=data[0]
    cur_address = {'id':data[0], 'text':data[1], 'city_id':data[2], 'user_id':data[3], 'geo_x':data[4], 'geo_y':data[5]}
    if cur_address['user_id'] != cur_user_id:
        return render(request, template, {'error_message':'this address don\'t belong to you!'})

    if request.method!='POST':
        print(cur_address)
        return render(request, template, {'address':cur_address})


    for field in ['city_id', 'text', 'geo_x', 'geo_y']:
        if not post_validator(request,field):
            return render(request, template, {'error_message' : 'invalid post form : '+field, 'address':cur_address})
    try:
        geo_x=float(request.POST['geo_x'])
        geo_y=float(request.POST['geo_y'])
    except:
        return render(request, template, {'error_message':'geo_x geo_y bad format'})
    new_address = {'id':cur_address['id'] , 'user_id':cur_user_id, 'city_id': int(request.POST['city_id']), 'text':request.POST['text'], 'geo_x':geo_x, 'geo_y':geo_y}
    cursor.execute(f"UPDATE Address SET city_id={request.POST['city_id']} text='{request.POST['text']}' geo_x={request.POST['geo_x']} geo_y={request.POST['geo_y']} where id ={address_id}")

    return HttpResponseRedirect(reverse('shop:address', kwargs={'address_id':address_id}))

def order(request, order_id):
    template = 'shop/order.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])

    cur_order = False


    cursor.execute(f"select * from Order where user_id={cur_user_id}")
    data=cursor.fetchall()
    if not data:
        return render(request, template, {'error_message':'wrong order id'})
    cur_order={'id':data[0], 'user_id':data[1], 'shop_id':data[2], 'address_id':data[3], 'dis_id':data[4], 'comment_id':data[5], 'status':data[6]}
    if cur_order['user_id'] != cur_user_id:
        return render(request, template, {'error_message':'this order don\'t belong to you!'})

    if request.method!='POST':
        return render(request, template, {'order':cur_order})
    #else do comment job

    for field in ['rate', 'text']:
        if not post_validator(request,field):
            return render(request, template, {'error_message' : 'invalid post form : '+field, 'order':cur_order})

    # if no comment
    try:
        rate = int(request.POST['rate'])
        if rate>5 or rate<1:
            raise 1
    except:
        return render(request, template, {'error_message':'invalid rate format', 'order':cur_order})
    new_comment = {'id':len(db_comments)+1, 'rate':rate, 'text':request.POST['text']}

    cursor.execute(f"INSERT INTO Comment (rate, text) VALUES ({request.POST['rate']}, '{request.POST['text']}')")
    cursor.execute(f"SELECT * FROM Commment where text='{request.POST['text']}' and rate={request.POST['rate']}")
    new_comment_id = cursor.fetchall()[0][0]
    cursor.execute(f"UPDATE Order SET comment_id={new_comment_id} where id = {order_id}")
    #TODO show comments of order
    return HttpResponseRedirect(reverse('shop:order', kwargs={'order_id' : order_id}))

def orders(request):
    template = 'shop/orders.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])

    cursor.execute(f"SELECT * FROM Order where user_id={cur_user_id}")
    data = cursor.fetchall()
    user_orders = [{'id':dat[0], 'user_id':dat[1], 'shop_id':dat[2], 'address_id':dat[3], 'dis_id':dat[4], 'comment_id':dat[5], 'status':dat[6]} for dat in data]
    return render(request, template, {'orders':user_orders})


def finalize(request):
    template = 'shop/finalize.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])



    cursor.execute(f"select FoodUserRelation.*, Food.shop_id, Food.price*(100-Food.discount)/100 from FoodUserRelation join Food on FoodUserRelation.food_id = Food.id and FoodUserRelation.user_id= {cur_user_id}")
    res = cursor.fetchall()

    if not res:
        return render(request, template, {'error_message': 'no item to buy'})
    user_items = [{'id':dat[0], 'food_id':dat[2], 'count':dat[3],'shop_id':dat[-2], 'discounted_price':dat[-1]} for dat in res]
    if request.method != 'POST':
        return render(request, template, {'items': user_items})

    #request is post

    for field in ['address_id']:
        if not post_validator(request, field):
            return render(request, template, {'error_message' : 'invalid post form : '+field,'items': user_items})

    try:
        cur_address_id = int(request.POST['address_id'])
    except:
        return render(request, template, {'error_message' : 'invalid address form', 'items': user_items})


    cursor.execute(f"SELECT * from Address WHERE user_id={str(cur_user_id)} and id={request.POST['address_id']}")
    res = cursor.fetchall()
    if not res:
        return render(request, template, {'error_message' : 'bad address', 'items': user_items})

    if 'discount_code' not in request.POST :
        return render(request, template, {'error_message' : 'missing discount_code in post', 'items': user_items})
    if request.POST['discount_code']:


        cursor.execute(f"SELECT Discount.id, Discount.percent from Discount join DiscountUserRelation on Discount.id = DiscountUserRelation.dis_id where Discount.code ='{request.POST['discount_code']}' and DiscountUserRelation.user_id IS NULL or DiscountUserRelation.user_id={cur_user_id}")
        data = cursor.fetchall()
        # if not cur_discount:
        if not data:
            return render(request, template, {'error_message' : 'invalid discount code', 'items': user_items})
        data=data[0]
        cur_discount = {'id':data[0], 'percent':data[1]}


        cursor.execute(f"SELECT * FROM Order WHERE discount_id={cur_discount['id']}")
        data = cursor.fetchall()
        # if bad_order:
        if data:
            return render(request, template, {'error_message' : 'you used this before', 'items': user_items})
        cur_discount_id = cur_discount['id']
        cursor.execute(f"INSERT INTO Order (user_id, shop_id, address_id, dis_id, comment_id, status) VALUES ({cur_user_id}, {user_items[0]['shop_id']}, {request.POST['address_id']}, {cur_discount_id}, NULL, 0)")

    else:
        cur_discount_id = 0
        cursor.execute(f"INSERT INTO Order (user_id, shop_id, address_id, dis_id, comment_id, status) VALUES ({cur_user_id},{user_items[0]['shop_id']}, {request.POST['address_id']}, NULL, NULL, 0)")


    cursor.execute(f"select * from orders where order.id={cur_user_id}")
    cur_order_id = cursor.fetchall()[-1][0]

    cursor.execute(f"INSERT INTO OrderFoodRelation(food_id, order_id, count) SELECT FoodUserRelation.food_id,{cur_order_id},FoodUserRelation.count from FoodUserRelation where FoodUserRelation.user_id ={cur_user_id}")

    cursor.execute(f"DELETE FROM FoodUserRelation WHERE FoodUserRelation.user_id={cur_user_id}")
    return HttpResponseRedirect(reverse('shop:order', kwargs={'order_id':cur_order_id}))

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

    # for user in db_users:
    #     if user['email'] == request.POST['email']:
    #         return render(request, template, {'error_message' : 'invalid post : you registered before'})

    #
    # new_user_id = len(db_users)+1
    # db_users.append({'id': new_user_id, 'first_name': request.POST['first_name'], 'last_name': request.POST['last_name'], 'email': request.POST['email'], 'password': request.POST['password'], 'phone_number':request.POST['phone_number']})

    cursor.execute("select * from User where email ='" + request.POST['email']+"'")
    res = cursor.fetchall()
    if res:
        return render(request, template, {'error_message' : 'invalid post : you registered before'})
    cursor.execute("INSERT INTO User (first_name, last_name, password, email , phone_number) VALUES ('" +request.POST['first_name']+"' , '"+request.POST['last_name']+"' , '"+request.POST['password']+"' , '"+request.POST['email']+"' , '"+request.POST['phone_number']+"' )")
    cursor.execute("select * from User where email='"+request.POST['email']+"'")
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

    # cur_user = False
    # for user in db_users:
    #     if user['email'] == request.POST['email'] and user['password'] == request.POST['password']:
    #         cur_user = user
    #         break
    cursor.execute("select * from User where email='"+ request.POST['email'] +"' and password='"+ request.POST['password'] +"'")
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
    cursor.execute("select * from User where User.id="+str(cur_user_id))
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

    # cur_user['first_name'] = request.POST['first_name']
    # cur_user['last_name'] = request.POST['last_name']
    # cur_user['phone_number'] = request.POST['phone_number']
    cursor.execute("UPDATE User SET first_name = '"+request.POST['first_name']+"' , last_name = '"+request.POST['last_name']+"' , phone_number = '"+request.POST['phone_number']+"' WHERE id = "+str(cur_user_id))


    cursor.execute("select * from User where User.id="+str(cur_user_id))
    data = cursor.fetchone()
    cur_user= {'id':data[0], 'first_name':data[1], 'last_name':data[2], 'email':data[4], 'phone_number':data[5]}
    return render(request, template, {'user':cur_user})


def dashboard(request):
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    template='shop/dashboard.html'
    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    # cur_user = False
    # for user in db_users:
    #     if user['id'] == cur_user_id:
    #         cur_user = user
    #         break
    #
    # if not cur_user:
    #     return render(request, template, {'error_message':'some thing wrong with cookies', 'cities':db_cities})
    cursor.execute("select * from User where User.id="+str(cur_user_id))
    data = cursor.fetchone()
    cur_user= {'id':data[0], 'first_name':data[1], 'last_name':data[2], 'email':data[4], 'phone_number':data[5]}
    return render(request, template, {'cities':db_cities, 'user':cur_user})


def shops_city(request, city_id):
    # cur_city = False
    # for city in db_cities:
    #     if city['id'] == city_id:
    #         cur_city = city
    #         break
    #
    # if not cur_city:
    #     return render(request, 'shop/shops.html', {'error_message':'invalid city id'})

    cursor.execute('select * from City where id='+str(city_id))
    res = cursor.fetchall()
    if not res:
        return render(request, 'shop/shops.html', {'error_message':'invalid city id'})
    # city_shops = []
    # for shop in db_shops:
    #     print(shop)
    #     if shop['city_id'] == cur_city['id']:
    #         city_shops.append(shop)

    cursor.execute("select * from Shop where city_id="+str(city_id))
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
    # cur_shop = False
    # for shop in db_shops:
    #     if shop['id'] == shop_id:
    #         cur_shop = shop
    #         break
    #
    # if not cur_shop:
    #     return render(request, template, {'error_message':'wrong shop id'})

    cursor.execute("select * from Shop where id="+str(shop_id))
    res = cursor.fetchall()
    if not res:
        return render(request, template, {'error_message':'wrong shop id'})
    # shop_foods=[]
    # for food in db_foods:
    #     if food['shop_id'] == shop_id:
    #         shop_foods.append(food)
    #shop_foods -> with discounted_price
    cursor.execute("select * from Food where shop_id="+str(shop_id))
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

    # cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    # cur_user = False
    # for user in db_users:
    #     if user['id'] == cur_user_id:
    #         cur_user = user
    #         break
    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    cursor.execute("select * from User where User.id="+str(cur_user_id))
    data = cursor.fetchone()
    cur_user= {'id':data[0], 'first_name':data[1], 'last_name':data[2], 'email':data[4], 'phone_number':data[5]}
    for field in ['food_id', 'count']:
        if not post_validator(request,field):
            return render(request, template, {'error_message' : 'invalid post form : '+field, 'shop':cur_shop, 'foods' : shop_foods})
    try:
        food_id = int(request.POST['food_id'])
        count = int(request.POST['count'])
        if count not in [1,-1]:
            raise 1
    except:
        return render(request, template, {'error_message':'geo_x geo_y bad format', 'shop':cur_shop, 'foods':shop_foods})

    # cur_item = False
    # for item in db_got_in_chart:
    #     if item['food_id'] == food_id and item['user_id'] == cur_user_id:
    #         cur_item = item
    cursor.execute("select * from FoodUserRelation where food_id="+str(food_id)+" and user_id= "+ str(cur_user_id))
    res = cursor.fetchall()

    if not res:
        if count == 1:
            # cur_item = {'id':len(db_got_in_chart)+1, 'user_id':cur_user_id, 'food_id':food_id, 'count':1}
            # db_got_in_chart.append(cur_item)
            cursor.execute("INSERT INTO FoodUserRelation ( user_id , food_id , count)VALUES ('"+str(cur_user_id)+"', "+str(food_id)+" , 1)")
        else:
            return render(request, template, {'error_message':'nothing to remove', 'shop':cur_shop,'foods':shop_foods})
    else:
        cur_count = res[0][3]
        cur_count += count
        if cur_count == 0:
            cursor.execute("delete from FoodUserRelation WHERE id = "+str(res[0][0]) )
        else:
            cursor.execute("UPDATE FoodUserRelation SET count = '"+str(cur_count)+"' WHERE id = "+str(res[0][0]))

    return render(request, template, {'shop':cur_shop, 'foods':shop_foods})


def addresses(request):
    template = 'shop/addresses.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    # cur_user = False
    # for user in db_users:
    #     if user['id'] == cur_user_id:
    #         cur_user = user
    #         break
    # if not cur_user:
    #     return render(request, template, {'error_message': 'my bad'})
    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    cursor.execute("select * from User where User.id="+str(cur_user_id))
    data = cursor.fetchone()
    cur_user= {'id':data[0], 'first_name':data[1], 'last_name':data[2], 'email':data[4], 'phone_number':data[5]}
    #
    # user_addresses = []
    # for address in db_addresses:
    #     if address['user_id'] == cur_user_id:
    #         user_addresses.append(address)
    cursor.execute("select * from Address where user_id="+str(cur_user_id))
    if request.method != "POST":
        return render(request, template, {'addresses':user_addresses})

    for field in ['city_id', 'text', 'geo_x', 'geo_y']:
        if not post_validator(request,field):
            return render(request, template, {'error_message' : 'invalid post form : '+field, 'addresses':cur_user_addresses})
    try:
        geo_x=float(request.POST['geo_x'])
        geo_y=float(request.POST['geo_y'])
    except:
        return render(request, template, {'error_message':'geo_x geo_y bad format'})
    # new_address = {'id':len(db_addresses)+1 ,'user_id':cur_user_id, 'city_id': int(request.POST['city_id']), 'text':request.POST['text'], 'geo_x':geo_x, 'geo_y':geo_y}
    # db_addresses.append(new_address)
    # user_addresses.append(new_address)
    cursor.execute("INSERT INTO Address ( text , city_id , geo_x , geo_y, user_id )VALUES ('"+request.POST['text']+"', "+request.POST['city_id']+" , "+request.POST['geo_x']+" , "+request.POST['geo_y']+", "+str(user_id)+");")
    return render(request, template, {'user_id':cur_user, 'addresses':user_addresses})


def address(request, address_id):
    template = 'shop/address.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    cur_user = False
    for user in db_users:
        if user['id'] == cur_user_id:
            cur_user = user
            break
    if not cur_user:
        return render(request, template, {'error_message': 'my bad'})

    cur_address = False
    for address in db_addresses:
        if address['id'] == address_id:
            cur_address = address
    if not cur_address:
        return render(request, template, {'error_message':'wrong address id'})
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
    #change address
    for x in cur_address:
        cur_address[x]=new_address[x]
    return render(request, template, {'address': cur_address})

def order(request, order_id):
    template = 'shop/order.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    cur_user = False
    for user in db_users:
        if user['id'] == cur_user_id:
            cur_user = user
            break
    if not cur_user:
        return render(request, template, {'error_message': 'my bad'})

    cur_order = False
    for order in db_orders:
        if order['user_id'] == cur_user_id:
            cur_order = order
    if not cur_order:
        return render(request, template, {'error_message':'wrong order id'})
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
    db_comments.append(new_comment)
    order['comment_id'] = new_comment['id']

    #TODO show comments of order
    return render(request, template, {'order':cur_order})


def orders(request):
    template = 'shop/orders.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    cur_user = False
    for user in db_users:
        if user['id'] == cur_user_id:
            cur_user = user
            break
    if not cur_user:
        return render(request, template, {'error_message': 'my bad'})

    user_orders = []

    for order in db_orders:
        if order['user_id'] == cur_user_id:
            user_orders.append(order)

    return render(request, template, {'orders':user_orders})


def finalize(request):
    template = 'shop/finalize.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    cur_user = False
    for user in db_users:
        if user['id'] == cur_user_id:
            cur_user = user
            break
    if not cur_user:
        return render(request, template, {'error_message': 'my bad'})

    user_items = []

    for item in db_got_in_chart:
        if item['user_id'] == cur_user_id:
            user_items.append(item)

    if not user_items:
        return render(request, template, {'error_message': 'no item to buy'})

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

    cur_address = False
    for address in db_addresses:
        if address['id'] == cur_address_id:
            cur_address = address
            break
    if cur_address['user_id'] != cur_user_id:
        return render(request, template, {'error_message' : 'bad address', 'items': user_items})

    if 'discount_code' not in request.POST :
        return render(request, template, {'error_message' : 'missing discount_code in post', 'items': user_items})
    if request.POST['discount_code']:
        cur_discount = False
        for discount in db_discounts:
            if discount['code'] == request.POST['discount_code']:
                cur_discount = discount
                break
        if not cur_discount:
            return render(request, template, {'error_message' : 'invalid discount code', 'items': user_items})

        cur_relation = False
        for relation in db_discount_user_relation:
            if relation['discount_id'] == cur_discount['id'] and (relation['user_id']==cur_user_id or relation['user_id']==0):
                cur_relation = relation
                break

        if not relation:
            return render(request, template, {'error_message' : 'this code doesn\'t belong to you', 'items': user_items})

        bad_order = False
        for order in db_orders:
            if order['discount_id'] == cur_discount['id']:
                bad_order = order
                break;
        if bad_order:
            return render(request, template, {'error_message' : 'you used this before', 'items': user_items})
        cur_discount_id = cur_discount['id']
    else:
        cur_discount_id = 0

    new_order = {'id':len(db_orders)+1, 'user_id':cur_user_id, 'discount_id':cur_discount_id, 'comment_id':0, 'status':0, 'address_id':cur_address['id']}
    db_orders.append(new_order)
    for item in user_items:
        db_order_food_relation.append({'id':len(db_order_food_relation)+1, 'order_id':new_order['id'], 'food_id':item['food_id'], 'count':item['count']})

    for item in user_items:
        #remove items
        pass
    return HttpResponseRedirect(reverse('shop:orders'))

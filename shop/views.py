from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from random import randint

import mysql.connector as mariadb
mariadb_connection = mariadb.connect(user='food_shop_user1', password='food_shop_user_password', database='food_shop')
cursor = mariadb_connection.cursor()

def flusher():
    cursor.execute("FLUSH TABLE")

active_cookies = {}#key user_id

def cities():
    cursor.execute(f"select * from City")
    data = cursor.fetchall()
    return [{'id':dat[0], 'name': dat[1], 'geo_x':dat[2], 'geo_y':dat[3]} for dat in data]

def user_addresses(user_id):
    cursor.execute(f"select * from Address where user_id={user_id}")
    data = cursor.fetchall()
    return [{'id':dat[0], 'text':dat[1], 'city_id':dat[2], 'user_id':dat[3], 'geo_x':dat[4], 'geo_y':dat[5]}for dat in data]

def user_by_id(user_id):
    cursor.execute(f"select * from User where User.id={user_id}")
    data = cursor.fetchone()
    return {'id':data[0], 'first_name':data[1], 'last_name':data[2], 'email':data[4], 'phone_number':data[5]}


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
    flusher()
    cursor.execute(f"select * from User where email='{request.POST['email']}'")
    new_user_id = cursor.fetchall()[0][0]
    t = loader.get_template('shop/login.html')
    content = {'logged_in': True, 'error_message':'you logged in'}
    response = HttpResponse(t.render(content, request))
    new_cookie = add_cookie(new_user_id)
    response.set_cookie('food-shop-cookie',str(new_cookie))

    return response


def login(request):
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
    if request.method!='POST':
        return render(request, template, {'user':user_by_id(cur_user_id)})

    for field in ['first_name', 'last_name', 'phone_number']:
        if not post_validator(request,field):
            return render(request, template, {'error_message' : 'invalid post form : '+field, 'user':user_by_id(cur_user_id)})

    for charr in request.POST['phone_number']:
        if charr not in '1234567890':
            return render(request, template, {'error_message' : 'invalid phone_number' , 'user':user_by_id(cur_user_id)})

    cursor.execute(f"UPDATE User SET first_name = '{request.POST['first_name']}' , last_name = '{request.POST['last_name']}' , phone_number = '{request.POST['phone_number']}' WHERE id = {cur_user_id}")
    flusher()

    return HttpResponseRedirect(reverse("shop:profile"))


def dashboard(request):
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    template='shop/dashboard.html'
    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])


    return render(request, template, {'cities':cities(), 'user':user_by_id(cur_user_id)})


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

    delta_x = f"(Shop.geo_x - {geo_x})"
    delta_y = f"(Shop.geo_y - {geo_y})"
    cursor.execute(f"SELECT * FROM Shop WHERE ({delta_x}*{delta_x}+{delta_y}*{delta_y})<50")
    data = cursor.fetchall()
    near_shops = [{'id':dat[0], 'name':dat[2],'aobut':dat[4]} for dat in data]
    return render(request, 'shop/shops.html', {'shops':near_shops})

def shop(request, shop_id):
    template = 'shop/shop.html'

    cursor.execute(f"select * from Shop where id={shop_id}")
    res = cursor.fetchall()
    if not res:
        return render(request, template, {'error_message':'wrong shop id'})

    dat=res[0]
    cur_shop = {'id': dat[0], 'city_id' : dat[1], 'name':dat[2], 'min_bill_val':dat[3], 'about':dat[4], 'address_text':dat[5], 'geo_x':dat[6], 'geo_y':dat[7]}

    logged_in = 0;
    foods=[]
    if 'food-shop-cookie' in request.COOKIES:
        print(request.COOKIES['food-shop-cookie'])
        if active_cookies.get(request.COOKIES['food-shop-cookie']):
            logged_in = 1;
            cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
            tmp1 = f"(select * from Food where Food.shop_id = {shop_id})"
            tmp2 = f"(select tmp1.*, Category.name as cat_name from {tmp1}tmp1 join Category on tmp1.cat_id = Category.id)"
            query = f"select tmp2.*, FoodUserRelation.count from FoodUserRelation right outer join {tmp2}tmp2 on tmp2.id = FoodUserRelation.food_id and FoodUserRelation.user_id = {cur_user_id}"
            cursor.execute(query)
            print(query)
            data=cursor.fetchall()
            print(data)
            foods = [{'id':dat[0], 'price': dat[3], 'name' : dat[4], 'discounted_price': (dat[3]*(100-dat[5])/100), 'about':dat[6],'cat_name':dat[7], 'count':dat[8] } for dat in data]
            print(foods)

    if not logged_in:
        tmp1 = f"(select * from Food where Food.shop_id = {shop_id})"
        tmp2 = f"(select tmp1.*, Category.name as cat_name from {tmp1}tmp1 join Category on tmp1.cat_id = Category.id)"
        cursor.execute(f"{tmp2}")
        data=cursor.fetchall()
        foods = [{'id':dat[0], 'price': dat[3], 'name' : dat[4], 'discounted_price': (dat[3]*(100-dat[5])/100), 'about':dat[6],'cat_name':dat[7] } for dat in data]


    if request.method != 'POST':
        return render(request, template, {'shop':cur_shop, 'foods':foods})
    #add or remove item
    #TODO dont buy from 2 shops
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cursor.execute(f"select Food.shop_id from FoodUserRelation join Food on FoodUserRelation.food_id=Food.id and FoodUserRelation.user_id={cur_user_id}")
    data= cursor.fetchall()
    if data and data[0][0] != shop_id:
        return render(request, template, {'shop':cur_shop, 'foods':foods, 'error_message':"not order with two shops"})
    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
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

    cursor.execute(f"select * from FoodUserRelation where food_id={food_id} and user_id={cur_user_id}")
    res = cursor.fetchall()

    if not res:
        if count == 1:
            cursor.execute(f"INSERT INTO FoodUserRelation ( user_id , food_id , count)VALUES ({cur_user_id},{food_id},1)")
            flusher()
        else:
            return render(request, template, {'error_message':'nothing to remove', 'shop':cur_shop,'foods':foods})
    else:
        cur_count = res[0][3]
        cur_count += count
        if cur_count == 0:
            cursor.execute(f"delete from FoodUserRelation WHERE id = {res[0][0]}")
            flusher()
        else:
            cursor.execute(f"UPDATE FoodUserRelation SET count = {cur_count} WHERE id = {res[0][0]}")
            flusher()
    return HttpResponseRedirect(reverse('shop:shop', kwargs={'shop_id':shop_id}))


def addresses(request):
    template = 'shop/addresses.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])
    if request.method != "POST":
        return render(request, template, {'addresses':user_addresses(cur_user_id), 'cities':cities()})


    for field in ['city_id', 'text', 'geo_x', 'geo_y']:
        if not post_validator(request,field):
            return render(request, template, {'error_message' : 'invalid post form : '+field, 'addresses':user_addresses(cur_user_id)})
    try:
        geo_x=float(request.POST['geo_x'])
        geo_y=float(request.POST['geo_y'])
    except:
        return render(request, template, {'error_message':'geo_x geo_y bad format'})

    cursor.execute(f"INSERT INTO Address ( text , city_id , geo_x , geo_y, user_id )VALUES ('{request.POST['text']}',{request.POST['city_id']},{request.POST['geo_x']} ,{request.POST['geo_y']},{cur_user_id})")
    flusher()
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
        return render(request, template, {'address':cur_address, 'cities':cities()})


    for field in ['city_id', 'text', 'geo_x', 'geo_y']:
        if not post_validator(request,field):
            return render(request, template, {'error_message' : 'invalid post form : '+field, 'address':cur_address, 'cities':cities()})
    try:
        geo_x=float(request.POST['geo_x'])
        geo_y=float(request.POST['geo_y'])
    except:
        return render(request, template, {'error_message':'geo_x geo_y bad format','address':cur_address, 'cities':cities()})
    new_address = {'id':cur_address['id'] , 'user_id':cur_user_id, 'city_id': int(request.POST['city_id']), 'text':request.POST['text'], 'geo_x':geo_x, 'geo_y':geo_y}
    cursor.execute(f"UPDATE Address SET city_id={request.POST['city_id']}, text='{request.POST['text']}', geo_x={request.POST['geo_x']}, geo_y={request.POST['geo_y']} where id ={address_id}")
    flusher()
    return HttpResponseRedirect(reverse('shop:address', kwargs={'address_id':address_id}))

def order(request, order_id):
    template = 'shop/order.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])

    cur_order = False


    cursor.execute(f"select * from food_shop.Order where id={order_id}")
    data=cursor.fetchall()
    if not data:
        return render(request, template, {'error_message':'wrong order id'})
    data = data[0]
    cur_order={'id':data[0], 'user_id':data[1], 'address_id':data[2], 'dis_id':data[3], 'comment_id':data[4], 'status':data[5]}

    if cur_order['user_id'] != cur_user_id:
        return render(request, template, {'error_message':'this order don\'t belong to you!'})
    if cur_order['comment_id']:
        cursor.execute(f"SELECT * FROM Comment WHERE id={cur_order['comment_id']}")
        data = cursor.fetchall()
        dat = data[0]
        comment = {'rate': dat[1], 'text':dat[2]}
        return render(request, template, {'order':cur_order, 'comment':comment})
    if request.method!='POST':
        return render(request, template, {'order':cur_order})
    #else do comment job

    for field in ['rate', 'text']:
        if not post_validator(request,field):
            return render(request, template, {'error_message' : 'invalid post form : '+field, 'order':cur_order})

    try:
        rate = int(request.POST['rate'])
        if rate>5 or rate<1:
            raise 1
    except:
        return render(request, template, {'error_message':'invalid rate format', 'order':cur_order})
    new_comment = {'rate':rate, 'text':request.POST['text']}

    cursor.execute(f"INSERT INTO Comment (rate, text) VALUES ({rate}, '{request.POST['text']}')")
    flusher()
    cursor.execute(f"SELECT * FROM Comment where text='{request.POST['text']}' and rate={rate}")
    new_comment_id = cursor.fetchall()[0][0]
    cursor.execute(f"UPDATE food_shop.Order SET comment_id={new_comment_id} where id = {order_id}")
    flusher()
    #TODO show comments of order
    return HttpResponseRedirect(reverse('shop:order', kwargs={'order_id' : order_id}))

def orders(request):
    template = 'shop/orders.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])

    cursor.execute(f"SELECT * FROM food_shop.Order where user_id={cur_user_id}")
    data = cursor.fetchall()
    user_orders = [{'id':dat[0], 'user_id':dat[1], 'address_id':dat[2], 'dis_id':dat[3], 'comment_id':dat[4], 'status':dat[5]} for dat in data]
    return render(request, template, {'orders':user_orders})


def finalize(request):
    template = 'shop/finalize.html'
    if 'food-shop-cookie' not in request.COOKIES:
        return HttpResponseRedirect(reverse('shop:login'))
    if not active_cookies.get(request.COOKIES['food-shop-cookie']):
        return HttpResponseRedirect(reverse('shop:login'))

    cur_user_id = active_cookies.get(request.COOKIES['food-shop-cookie'])

    cursor.execute(f"select FoodUserRelation.*, Food.shop_id, Food.price*(100-Food.discount)/100 ,Food.name from FoodUserRelation join Food on FoodUserRelation.food_id = Food.id and FoodUserRelation.user_id= {cur_user_id}")
    res = cursor.fetchall()
    if not res:
        return render(request, template, {'error_message': 'no item to buy'})
    foods = [{'id':dat[0], 'food_id':dat[2], 'count':dat[3],'shop_id':dat[-3], 'discounted_price':dat[-2], 'name':dat[-1]} for dat in res]
    if request.method != 'POST':
        return render(request, template, {'foods':foods, 'addresses':user_addresses(cur_user_id)})

    #request is post

    for field in ['address_id']:
        if not post_validator(request, field):
            return render(request, template, {'error_message' : 'invalid post form : '+field,'foods':foods, 'addresses':user_addresses(cur_user_id)})

    try:
        cur_address_id = int(request.POST['address_id'])
    except:
        return render(request, template, {'error_message' : 'invalid address form', 'foods':foods, 'addresses':user_addresses(cur_user_id)})


    cursor.execute(f"SELECT * from Address WHERE user_id={str(cur_user_id)} and id={request.POST['address_id']}")
    res = cursor.fetchall()
    if not res:
        return render(request, template, {'error_message' : 'bad address', 'foods':foods, 'addresses':user_addresses(cur_user_id)})

    if 'discount_code' not in request.POST :
        return render(request, template, {'error_message' : 'missing discount_code in post', 'foods':foods, 'addresses':user_addresses(cur_user_id)})
    if request.POST['discount_code']:

        cursor.execute(f"SELECT Discount.id, Discount.percent from Discount join DiscountUserRelation on Discount.id = DiscountUserRelation.dis_id where Discount.code ='{request.POST['discount_code']}' and DiscountUserRelation.user_id IS NULL or DiscountUserRelation.user_id={cur_user_id}")
        data = cursor.fetchall()
        # if not cur_discount:
        if not data:
            return render(request, template, {'error_message' : 'invalid discount code', 'foods':foods, 'addresses':user_addresses(cur_user_id)})
        data=data[0]
        cur_discount = {'id':data[0], 'percent':data[1]}


        cursor.execute(f"SELECT * FROM food_shop.Order WHERE dis_id={cur_discount['id']}")
        data = cursor.fetchall()
        # if bad_food_shop:
        if data:
            return render(request, template, {'error_message' : 'you used this before', 'foods':foods, 'addresses':user_addresses(cur_user_id)})
        cur_discount_id = cur_discount['id']
        query = f"INSERT INTO food_shop.Order (user_id, address_id, dis_id, comment_id, status) VALUES ({cur_user_id}, {request.POST['address_id']}, {cur_discount_id}, NULL, 0)"
        print(query)
        cursor.execute(query)
        flusher()
    else:
        cur_discount_id = 0
        query = f"INSERT INTO food_shop.Order (user_id, address_id, dis_id, comment_id, status) VALUES ({cur_user_id}, {request.POST['address_id']}, NULL, NULL, 0)"
        print(query)
        cursor.execute(query)
        flusher()

    cursor.execute(f"select * from food_shop.Order where Order.user_id={cur_user_id}")
    cur_order_id = cursor.fetchall()[-1][0]

    cursor.execute(f"INSERT INTO OrderFoodRelation(food_id, order_id, count) SELECT FoodUserRelation.food_id,{cur_order_id},FoodUserRelation.count from FoodUserRelation where FoodUserRelation.user_id ={cur_user_id}")
    flusher()
    cursor.execute(f"DELETE FROM FoodUserRelation WHERE FoodUserRelation.user_id={cur_user_id}")
    flusher()
    return HttpResponseRedirect(reverse('shop:order', kwargs={'order_id':cur_order_id}))

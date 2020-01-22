from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from random import randint

active_cookies = {}#key user_id

def add_cookie(user_id):
    new_cookie = randint(100000000000000000000000,100000000000000000000000*10-1)
    while(new_cookie in active_cookies):
        new_cookie = randint(100000000000000000000000,100000000000000000000000*10-1)
    active_cookies.update({new_cookie, user_id})
    print('adddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
    return new_cookie


def hello(request):
    response = HttpResponse("Hello World!")
    response.set_cookie('salam','salam')
    return response



def register(request):
    template='shop/register.html'
    if not request.method == 'POST':
        return render(request, template, {})

    #do sth with request.POST['KEY']
    return render(request, template, {})


def login(request):
    template='shop/login.html'
    if request.method != 'POST' or 'username' not in request.POST or 'password' not in request.POST:
        return render(request, template, {})


    all_users = {('ali','ali')}
    if (request.POST['username'],request.POST['password']) not in all_users:
        return render(request, template, {'error_message' : "Wrong username or password"})

    user_id = 1

    t = loader.get_template(template)
    content = {'logged_in': 1}
    response = HttpResponse(t.render(content, request))
    new_cookie = add_cookie(user_id)
    response.set_cookie('food-shop-cookie',str(new_cookie))

    return response

def logout(request):
    template='shop/logout.html'

    #logout

    return HttpResponseRedirect(reverse('shop:login'))


def dashboard(request):
    template='shop/dashboard.html'
    print(request.COOKIES)

    # if request.POST['user'] not in active_users:
    #     return HttpResponseRedirect(reverse('shop:login'))

    return render(request, template, {})


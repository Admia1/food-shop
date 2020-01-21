from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def hello(request):
    return HttpResponse("Hello World!")



def register(request):
    template='shop/register.html'
    if not request.method == 'POST':
        return render(request, template, {})

    #do sth with request.POST['KEY']
    return render(request, template, {})


def login(request):
    template='shop/login.html'
    if not request.method == 'POST':
        return render(request, template, {})

    #do sth with request.POST['KEY']
    return render(request, template, {})


def logout(request):
    template='shop/logout.html'

    #logout

    return HttpResponseRedirect(reverse('shop:login'))


def dashboard(request):
    template='shop/dashboard.html'

    # if request.POST['user'] not in active_users:
    #     return HttpResponseRedirect(reverse('shop:login'))

    return render(request, template, {})

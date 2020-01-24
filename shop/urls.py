from . import views
from django.urls import path

app_name = "shop"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('addresses/', views.addresses, name='addresses'),
    path('address/<int:address_id>/', views.address, name='address'),

    path('shops/city/<int:city_id>/', views.shops_city, name='shops_city'),
    path('shops/location/', views.shops_location, name='shops_location'),
    path('shop/<int:shop_id>/', views.shop, name='shop'),    # add and remove food -> do it on shop with post

    path('orders/', views.orders, name='orders'),
    path('order/<int:shop_id>/', views.order, name='order'),#use post to comment

    #todo search
]

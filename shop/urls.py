from . import views
from django.urls import path

app_name = "shop"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('shops/city/<int:city_id>/', views.shops_city, name='shops_city'),
    path('shops/location/', views.shops_location, name='shops_location'),
    path('shop/<int:shop_id>/', views.shop, name='shop'),
]

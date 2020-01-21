from . import views
from django.urls import path

app_name = "shop"

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

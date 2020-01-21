from . import views
from django.urls import path

app_name = "shop"

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]

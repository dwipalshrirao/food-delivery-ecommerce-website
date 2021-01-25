from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index,name='index'),
    path('base/',views.base),
    path('all-food/',views.all_food,name='all-food'),
    path('updatecart/',views.updatecart,name='updatecart'),
    path('cart/',views.order_cart,name='cart'),

    path('search/',views.search,name='search'),
   
   
]
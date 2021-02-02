from django.contrib import admin
from django.urls import path
from . import views
# app_name = "blogapp"
urlpatterns = [
    
    path('', views.blog_list,name='bloglist'),
    path('<int:id>',views.single_blog,name='singleblog'),
    path('subcribe/',views.subscribe,name='subscribe')
    
   
]
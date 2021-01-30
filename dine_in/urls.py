
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'dine_in'


urlpatterns = [
   
    path('',views.dine_in, name='dine_in'),
    path('otp_page/<str:email>/',views.otp_verification_page,name='otp_page'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
   

] 

#urlpatterns = [
    # ... the rest of your URLconf goes here ...
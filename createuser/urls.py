from django.urls import path
from createuser import views
# SET THE NAMESPACE!
app_name = 'createuser'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('registration/',views.unverified_email,name='register'),
    path('otp/<str:email>',views.verify_otp,name='verify_otp'),
    path('',views.user_login,name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('checkmail/', views.check_email,name='checkmail'),
    path('regenotp/', views.regenrate_otp,name='regenrate_otp'),

]
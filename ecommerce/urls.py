"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages.views import flatpage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls'),name ='products'),
    path('login/',include('createuser.urls')),
    path('blogs/',include('blogapp.urls'),name='blogapp'),
    path('dinein/',include('dine_in.urls'),name ='dinein'),
    path('about-us/', flatpage, {'url': '/about/'}, name='about'),
    # path('pages/', include('django.contrib.flatpages.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#urlpatterns = [
    # ... the rest of your URLconf goes here ...
from django.contrib import admin

# Register your models here.
from .models import product,cart,category

class adminproduct(admin.ModelAdmin):
    list_display=['pname','price','disc_price', 'pslug']



admin.site.register(product,adminproduct)

class admincart(admin.ModelAdmin):
    list_display=['user','productid']

admin.site.register(cart,admincart)
admin.site.register(category)
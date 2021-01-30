from django.contrib import admin

# Register your models here.
from .models import table_booking


class admintable(admin.ModelAdmin):
    list_display=['email','people','booking_time']

admin.site.register(table_booking,admintable)
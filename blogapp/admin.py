from django.contrib import admin

# Register your models here.
from .models import blog,subscribed_email

class adminblog(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.author = request.user.first_name
        super().save_model(request, obj, form, change)

admin.site.register(blog,adminblog)


class adminsub_email(admin.ModelAdmin):
    list_display=('email','subscribe_time')
admin.site.register(subscribed_email,adminsub_email)
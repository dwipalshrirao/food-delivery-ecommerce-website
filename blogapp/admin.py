from django.contrib import admin

# Register your models here.
from .models import blog

class adminblog(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.author = request.user.first_name
        super().save_model(request, obj, form, change)

admin.site.register(blog,adminblog)
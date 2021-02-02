from django.db import models

# Create your models here.



class blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    image=models.ImageField(upload_to="images/blogs")    
    created_date=models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=30,null=True,blank=True)

    

    def __str__(self):
        return self.title

class subscribed_email(models.Model):
    email=models.EmailField(max_length=100)
    subscribe_time=models.DateTimeField(auto_now_add=True)
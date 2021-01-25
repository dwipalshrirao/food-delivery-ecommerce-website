from django.db import models

# Create your models here.


class blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    image=models.ImageField(upload_to="images/blogs")    
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
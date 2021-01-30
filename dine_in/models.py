from django.db import models

# Create your models here.

class table_booking(models.Model):
    email=models.CharField(max_length=100)
    booking_time=models.DateTimeField()
    people=models.PositiveIntegerField(null=True,blank=True)
    booked=models.BooleanField(null=True,blank=True)
    otp=models.CharField(max_length=10,null=True,blank=True)
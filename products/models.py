from django.db import models


# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=20,null=True)

    @property
    def get_products(self):
        return product.objects.filter(categories__name=self.name)

    def __str__(self):
        return self.name



class product(models.Model):
    CATEGORY=(
    ('veg', 'veg'),
    ('non-veg', 'non-veg'),
    ('breackfast', 'breackfast')
)
    pname= models.CharField(max_length=40)
    pimage=models.ImageField(upload_to="images/products")
    price=models.FloatField()
    disc_price=models.FloatField(default=0)
    # category = models.CharField(max_length=20,null=True)
    categories = models.ForeignKey(category, on_delete=models.SET_NULL,null=True)
    pslug=models.SlugField(max_length=20)


class cart(models.Model):
    user=models.CharField(max_length=40,null=True,blank=True)
    mobile_id=models.CharField(max_length=100,null=True,blank=True)
    productid=models.CharField(max_length=200,null=True,blank=True)
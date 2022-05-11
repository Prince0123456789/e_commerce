from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=16)
    email=models.EmailField()
    mob=models.IntegerField()
    def __str__(self):
        return self.username

class product(models.Model):
    proname=models.CharField(max_length=15)
    proid=models.IntegerField()
    procategory=models.CharField(max_length=20)
    proprice=models.FloatField()
    proimage=models.ImageField(upload_to='shop1/images')
    def __str__(self):
        return self.proname

class cart_items(models.Model):
    item_user=models.CharField(max_length=20)
    item_name=models.CharField(max_length=20)
    item_price=models.FloatField()
    def __str__(self):
        return self.item_name+" "+self.item_user
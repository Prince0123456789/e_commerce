from django.contrib import admin

# Register your models here.
from shop1 import models

admin.site.register(models.user)
admin.site.register(models.product)
admin.site.register(models.cart_items)

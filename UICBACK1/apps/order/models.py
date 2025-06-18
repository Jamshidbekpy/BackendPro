from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.

class Product(models.Model):
    name = models.CharField(_('Name'),max_length=255)
    price = models.DecimalField(_('Price'),max_digits=10,decimal_places=2)
    is_active = models.BooleanField(_('Is_active'),default=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(_('Name'),max_length=255)
    user = models.ForeignKey(get_user_model(),on_delete=models.PROTECT, related_name='order')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT, related_name='order_items')
    product = models.ForeignKey(Product,on_delete=models.PROTECT, related_name='order_items')
    quantity = models.PositiveIntegerField(_('Quantity'),default=1)
    
   
    
class OrderItemConfig(models.Model):
    order_item = models.ForeignKey(OrderItem,on_delete=models.PROTECT, related_name='order_conf')
    key = models.CharField(_('Key'),max_length=255)
    value = models.CharField(_('Value'),max_length=255)
    text = models.TextField()
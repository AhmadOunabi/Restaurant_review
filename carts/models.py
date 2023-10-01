from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from meals.models import Meal
# Create your models here.

class Cart(models.Model):
    user= models.OneToOneField(User,related_name='user_cart',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_cart(sender,instance,created,**kwargs):
        if created:
            Cart.objects.create(user=instance)



class CartProduct(models.Model):
    cart=models.ForeignKey(Cart,related_name='cart_products',on_delete=models.CASCADE)
    product= models.ForeignKey(Meal,related_name='cart_meal', on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return str(self.cart)
    
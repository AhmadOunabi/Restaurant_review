from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
# Create your models here.

class Meal(models.Model):
    
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    description=models.TextField(max_length=500)
    
    def __str__(self):
        return self.name



class Review(models.Model):
    user=models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True,blank=True)
    meal=models.ForeignKey(Meal,related_name='meal_review',on_delete=models.CASCADE)
    review=models.CharField(max_length=500)
    rate=models.IntegerField(default=2)
    create_date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.meal.name
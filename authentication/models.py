from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User,related_name='User_profile',on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.user
    
    # Create new Profile for each new User
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
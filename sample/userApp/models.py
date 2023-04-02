from django.db import models
from django.utils import timezone
from datetime import datetime
from django.conf import settings


class User(models.Model):
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=10)
    user_creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40,blank=True)
    image = models.ImageField(blank=True)
   
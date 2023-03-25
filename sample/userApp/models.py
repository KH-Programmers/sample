from django.db import models
from django.utils import timezone
from datetime import datetime



class User(models.Model):
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=10)
    user_creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id
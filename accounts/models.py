from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=150)



    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '
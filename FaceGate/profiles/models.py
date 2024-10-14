from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(blank=False,upload_to='photos')


    def __str__(self):
        return f"profile of {self.user.username}"
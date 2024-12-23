from django.db import models
from django.contrib.auth.models import User
from django.utils import  timezone



class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True, max_length=2000)
    avatar = models.ImageField(upload_to='avaters/', blank=True, null=True, default='download.jpeg')
    created = models.DateTimeField(default=timezone.now)
    modifiyed = models.DateTimeField(default=timezone.now)
    available = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.user.username

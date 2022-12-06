from django.db import models
from django.contrib.auth.models import User

class Host(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="host")
    profile_img = models.URLField(max_length=300, blank=True)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
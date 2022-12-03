from django.db import models
from django.contrib.auth.models import User

class Host(models.Model):
    
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    profile_img = models.URLField(max_length=300, blank=True)
    description = models.TextField(max_length=500, blank=True)
    photo_id = models.ForeignKey("Photo", on_delete=models.CASCADE)
    location_id = models.ForeignKey("Location", on_delete=models.CASCADE)
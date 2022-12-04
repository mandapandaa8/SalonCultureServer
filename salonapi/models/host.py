from django.db import models
from django.contrib.auth.models import User

class Host(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="host")
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    photo_id = models.ForeignKey("Photo", on_delete=models.CASCADE, related_name="host")
    location_id = models.ForeignKey("Location", on_delete=models.CASCADE, related_name="host")
from django.db import models
from django.contrib.auth.models import User\

class Artist(models.Model):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="artist")
    medium = models.CharField(max_length=30, blank=True)
    cv = models.TextField(max_length=500, blank=True)
    location_id = models.ForeignKey("Location", on_delete=models.CASCADE, related_name="artist")
from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):

    photo_url = models.URLField(max_length=300)
    caption = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photos")
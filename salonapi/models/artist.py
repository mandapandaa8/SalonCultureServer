from django.db import models
from django.contrib.auth.models import User\

class Artist(models.Model):

    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    medium = models.CharField(max_length=30, blank=True)
    cv = models.TextField(max_length=500, blank=True)
    profile_image = models.URLField(max_length=300, blank=True)
    locationID = models.ForeignKey("Location", on_delete=models.CASCADE)



    def __str__(self):
        return self.name
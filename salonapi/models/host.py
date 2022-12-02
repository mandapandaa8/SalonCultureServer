from django.db import models
from django.contrib.auth.models import User

class Host(models.Model):
    
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    profileImg = models.URLField(max_length=300, blank=True)
    accommodationId = models.ForeignKey("Accommodation", on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    photoId = models.ForeignKey("Photo", on_delete=models.CASCADE)
    locationId = models.ForeignKey("Location", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
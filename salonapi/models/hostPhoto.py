from django.db import models

class HostPhoto(models.Model):

    photo_url = models.URLField(max_length=300)
    caption = models.CharField(max_length=300)
    host = models.ForeignKey("Host", on_delete=models.CASCADE, related_name="photo")
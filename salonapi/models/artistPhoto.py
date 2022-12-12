from django.db import models

class ArtistPhoto(models.Model):

    photo_url = models.URLField(max_length=300)
    caption = models.CharField(max_length=300)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE, related_name="photo")
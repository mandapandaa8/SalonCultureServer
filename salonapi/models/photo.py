from django.db import models

class Photo(models.Model):

    photo_url = models.URLField(max_length=300)
    caption = models.CharField(max_length=300)
    artist_id = models.ForeignKey("Artist", on_delete=models.CASCADE)
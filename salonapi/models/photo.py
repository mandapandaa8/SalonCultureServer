from django.db import models

class Photo(models.Model):

    photoURL = models.URLField(max_length=300)
    caption = models.CharField(max_length=300)
    artistId = models.ForeignKey("Artist", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
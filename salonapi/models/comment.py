from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):

    comment_text = models.CharField(max_length=300)
    artist_photo = models.ForeignKey("ArtistPhoto", on_delete=models.CASCADE, related_name="comments")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="comments")
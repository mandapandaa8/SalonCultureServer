from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):

    commentText = models.CharField(max_length=300)
    photoId = models.ForeignKey("Photo", on_delete=models.CASCADE)
    userID = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
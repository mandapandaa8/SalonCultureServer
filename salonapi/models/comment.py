from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):

    comment_text = models.CharField(max_length=300)
    photo_id = models.ForeignKey("Photo", on_delete=models.CASCADE)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
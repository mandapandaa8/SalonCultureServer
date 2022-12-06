from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="follower")
    follower = models.OneToOneField(User, on_delete=models.CASCADE, related_name="following")
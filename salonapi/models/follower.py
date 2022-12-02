from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):

    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    followerId = models.OneToOneField(User, on_delete=models.CASCADE)
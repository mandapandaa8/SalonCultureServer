from django.db import models
from django.contrib.auth.models import User

class User(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.URLField(max_length=300, blank=True)
from django.db import models

class Location(models.Model):
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
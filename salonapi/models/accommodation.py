from django.db import models

class Accommodation(models.Model):

    accommodationName = models.CharField(max_length=30)
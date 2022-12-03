from django.db import models

class Accommodation(models.Model):

    accommodation_name = models.CharField(max_length=30)
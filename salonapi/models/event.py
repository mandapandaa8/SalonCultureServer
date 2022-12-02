from django.db import models

class Event(models.Model):

    hostID = models.ForeignKey("Host", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    accommodationId = models.ForeignKey("Accommodation", on_delete=models.CASCADE)
    capacity = models.integerField()
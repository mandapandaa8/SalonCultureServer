from django.db import models

class Event(models.Model):

    host_id = models.ForeignKey("Host", on_delete=models.CASCADE, related_name="events")
    date = models.DateField()
    time = models.TimeField()
    accommodation_id = models.ForeignKey("Accommodation", on_delete=models.CASCADE, related_name="events")
    capacity = models.IntegerField()
from django.db import models

class Event(models.Model):

    host = models.ForeignKey("Host", on_delete=models.CASCADE, related_name="events")
    date = models.DateField()
    time = models.TimeField()
    accommodation = models.ForeignKey("Accommodation", on_delete=models.CASCADE, related_name="events")
    capacity = models.IntegerField()
    location = models.ForeignKey("Location", on_delete=models.CASCADE, related_name="events")
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):

    host = models.ForeignKey("Host", on_delete=models.CASCADE, related_name="events")
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    accommodation = models.ForeignKey("Accommodation", on_delete=models.CASCADE, default=0, related_name="events")
    details = models.TextField(max_length=500, blank=True)
    capacity = models.IntegerField()
    attendees = models.ManyToManyField("Artist", through="EventUser", related_name="events")
    

    @property
    def joined(self):
        return self.__joined

    @property
    def attendee_count(self):
        return self.attendees.count()

    @joined.setter
    def joined(self, value):
        self.__joined = value
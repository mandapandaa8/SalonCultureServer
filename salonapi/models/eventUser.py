from django.db import models
from django.contrib.auth.models import User

class EventUser(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="event_host")
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="event_user")
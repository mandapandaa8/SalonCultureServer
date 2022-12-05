from django.db import models
from django.contrib.auth.models import User

class EventUser(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_user")
    event_id = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="event_user")
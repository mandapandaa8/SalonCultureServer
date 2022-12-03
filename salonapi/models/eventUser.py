from django.db import models
from django.contrib.auth.models import User

class EventUser(models.Model):
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey("Event", on_delete=models.CASCADE)
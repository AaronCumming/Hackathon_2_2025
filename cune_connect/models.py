import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Organization(models.Model):
    organization_name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    regular_meeting_time = models.CharField(max_length=255)
    location_of_reg_meeting_time = models.CharField(max_length=255)

    def __str__(self):
        return self.organization_name
    
class Event(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=255)
    date = models.DateTimeField("date and time of event")
    image = models.ImageField(upload_to='cune_connect/images/', null=True, blank=True)

    def __str__(self):
        return self.event_name


    def up_coming_event(self):
        return self.date >= timezone.now() - datetime.timedelta(days=7)
    

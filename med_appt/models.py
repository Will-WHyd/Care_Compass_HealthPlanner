from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

STATUS = (
    ('Pending', 'Pending'),
    ('Attended', 'Attended'), 
    ('Cancelled', 'Cancelled'),
    ('Rescheduled', 'Rescheduled'),
)

# Create your models here.

class Consultant(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    specialty = models.CharField(max_length=100, null=False, blank=False, default='General Practitioner')
    institution = models.CharField(max_length=100, null=False, blank=False, default='No Institution/Hospital set')
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

# Model for creating appointments
class Appointment(models.Model):
    """
    Stores a single Appointment related to :model:`auth.user`
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    procedure = models.CharField(max_length=200)
    appt_date = models.DateField(default=timezone.localdate)
    appt_time = models.TimeField(auto_now=False, auto_now_add=False)
    address = models.TextField(max_length=200, null=True, blank=True)
    consultant = models.ForeignKey(Consultant, null=False, blank=False, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='Pending', max_length=20)
    details = models.TextField(null=True, blank=True)
    followup_details = models.TextField(null=True, blank=True)
    travel_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Appointment for {self.procedure} on {self.appt_date} at {self.appt_time}.'

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from user_profile.models import Profile
from phonenumber_field.modelfields import PhoneNumberField


STATUS = (
    ('Pending', 'Pending'),
    ('Attended', 'Attended'), 
    ('Cancelled', 'Cancelled'),
    ('Rescheduled', 'Rescheduled'),
)

# Create your models here.

class Consultant(models.Model):
    """
    Stores a single Consultant entry related to :model:`auth.User`. 
    in views.py, :model:`user_profile.profile` is associated with the Consultant on creation via 'clients'
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    specialty = models.CharField(max_length=100, null=False, blank=False, default='General Practitioner')
    institution = models.CharField(max_length=100, null=False, blank=False, default='No Institution/Hospital set')
    email = models.EmailField(max_length=200)
    contact_phone = PhoneNumberField(blank=True, null=True)
    details = models.TextField(null=True, blank=True)

    # Fields for managing across multiple users
    private = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    clients = models.ManyToManyField(Profile, related_name="consultants", blank=True)

    def __str__(self):
        return self.name

# Model for creating appointments
class Appointment(models.Model):
    """
    Stores a single Appointment related to :model:`auth.user` and :model:`appt.Consultant`
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    procedure = models.CharField(max_length=200)
    appt_date = models.DateField(default=timezone.localdate)
    appt_time = models.TimeField(auto_now=False, auto_now_add=False)
    address = models.TextField(max_length=200, null=True, blank=True)
    consultant = models.ForeignKey(Consultant, null=True, blank=True, on_delete=models.SET_NULL)
    consultant_name = models.CharField(max_length=100, blank=True, editable=False)
    status = models.CharField(choices=STATUS, default='Pending', max_length=20)
    details = models.TextField(null=True, blank=True)
    followup_details = models.TextField(null=True, blank=True)
    travel_details = models.TextField(null=True, blank=True)

    def save_name(self, *args, **kwargs):
        # Store the consultant's name in `consultant_name` for historical reference
        if self.consultant:
            self.consultant_name = self.consultant.name
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Appointment for {self.procedure} on {self.appt_date} at {self.appt_time}.'

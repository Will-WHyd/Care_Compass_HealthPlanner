from django.db import models
from django.contrib.auth.models import User


CONFIRMATION = (
    (0, 'Pending'),
    (1, 'Attended'), 
    (2, 'Cancelled'),
    (3, 'Rescheduled'),
)

# Create your models here.

class Appointment(models.Model):
    """
    Stores a single Appointment related to :model:`auth.user`
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    procedure = models.CharField(max_length=200, unique=True)
    appt_date = models.DateField(default=datetime.date.today)
    appt_time = models.TimeField(auto_now=False, auto_now_add=False)
    address = models.TextField(max_length=200, null=True, blank=True)
    consultant = models.ForeignKey(Consultant, null=False, blank=False, on_delete=models.CASCADE)
    status = models.CharField(choices=CONFIRMATION, default=0, max_length=50)
    details = models.TextField(null=True, blank=True)
    followup_details = models.TextField(null=True, blank=True)
    travel_details = models.TextField(null=True, blank=True)


class Consultant(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

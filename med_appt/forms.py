from django import forms
from .models import Appointment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "procedure", 
            "appt_date", 
            "appt_time", 
            "status", 
            "consultant", 
            "address", 
            "details", 
            "travel_details"
        ]

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Create Appointment'))

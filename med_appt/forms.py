from django import forms
from .models import Appointment, Consultant
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import datetime


class AppointmentForm(forms.ModelForm):
    """
    Form class for users to create an appointment. 
    """
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

        # Widgets for time/date selection on form
        widgets = {
            "appt_date": forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                }
            ),
            "appt_time": forms.TimeInput(
                attrs={'type': 'time',
                    'class': 'form-control',
                    'step': '300',}
            ),
        }
    

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)
        # set default time
        self.fields['appt_date'].initial = datetime.now().date()

        # Ensures users can only view public Consultants AND private consultants they have created
        if user is not None and hasattr (user, 'profile'):
            profile = user.profile
            self.fields['consultant'].queryset = Consultant.objects.filter(private=False) | Consultant.objects.filter(private=True, clients=profile)
        else:
            self.fields['consultant'].queryset = Consultant.objects.filter(private=False)

        # Configure crispy forms:
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Create Appointment'))


class ConsultantForm(forms.ModelForm):
    """
    Form class for users to create a Consultant. 
    """
    class Meta:
        model = Consultant
        fields = [
            "name",
            "specialty",
            "institution",
            "email",
            "contact_phone",
            "details",
            "private"
        ]

    def __init__(self, *args, **kwargs):
        super(ConsultantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Add Consultant'))

from django import forms
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "profile_image",
            "contact_phone", 
            "contact_email", 
            "info", 
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Update Details'))

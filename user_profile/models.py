from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    """
    Stores a single Profile page entry details
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    profile_image = CloudinaryField('image', default='placeholder')
    contact_phone = PhoneNumberField(null=True)
    contact_email = models.EmailField(blank=True, max_length=200)
    info = models.TextField(max_length=5000, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Profile page of {self.name}'



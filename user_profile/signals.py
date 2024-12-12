from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from med_appt.models import Appointment, Consultant

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # This ensures it only runs when a new User is created
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Appointment)
def associate_profile_with_consultant(sender, instance, created, **kwargs):
    if created:  # Ensure this runs only when a new Appointment is created
        consultant = instance.consultant
        user_profile = instance.user.profile

        if user_profile not in consultant.clients.all():
            consultant.clients.add(user_profile)


from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    list_display = ('user', 'name', 'contact_phone', 'contact_email')
    summernote_fields = ('info')
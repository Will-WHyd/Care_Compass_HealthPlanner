from django.contrib import admin
from .models import Appointment, Consultant

# Register your models here.
@admin.register(Appointment)
class ApptAdmin(admin.ModelAdmin):
    list_display = ('user', 'procedure', 'appt_date', 'consultant', 'status')
    list_filter = ['user', 'consultant', 'status']

@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'institution')
    list_filter = ['name', 'specialty', 'institution']


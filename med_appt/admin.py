from django.contrib import admin
from .models import Appointment, Consultant
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Appointment)
class ApptAdmin(SummernoteModelAdmin):
    list_display = ('user', 'procedure', 'appt_date', 'consultant', 'status')
    list_filter = ['user', 'consultant', 'status']
    search_fields = ['user', 'procedure', 'consultant']
    summernote_fields = ('details', 'followup_details',)

@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'institution')
    list_filter = ['name', 'specialty', 'institution']


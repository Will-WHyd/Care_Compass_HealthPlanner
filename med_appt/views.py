from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Appointment, Consultant

# Create your views here.
class ApptList(generic.ListView):
    """
    Displays list of appointments
    """
    queryset = Appointment.objects.all()
    template_name = 'appt/index.html'
    
def appt_detail(request, id):
    appt = get_object_or_404(Appointment, id=id)
    context = {
        'appt': appt,
    }
    return render(
        request, "appt/appt_detail.html", context,
    )
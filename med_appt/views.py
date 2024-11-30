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
    queryset = Appointment.objects.all().order_by('-appt_date')
    template_name = 'appt/index.html'
    paginate_by = 8
    
def appt_detail(request, id):
    appt = get_object_or_404(Appointment, id=id)
    context = {
        'appt': appt,
    }
    return render(
        request, "appt/appt_detail.html", context,
    )

# def appt_create(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.Post or None, request)
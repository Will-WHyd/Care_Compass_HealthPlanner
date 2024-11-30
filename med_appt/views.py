from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Appointment, Consultant
from .forms import AppointmentForm

# Create your views here.
class ApptList(LoginRequiredMixin, generic.ListView):
    """
    Displays list of appointments belonging to the logged-in user
    """
    model = Appointment
    template_name = 'appt/index.html'

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user).order_by('-appt_date')
    paginate_by = 8
    
@login_required
def appt_detail(request, id):
    appt = get_object_or_404(Appointment, id=id)

    if appt.user == request.user:
        context = {
            'appt': appt,
        }
        return render(
            request, "appt/appt_detail.html", context,
        )
    else:
        return render(request, "appt/403.html")

@login_required
def appt_create(request):
    appt_form = AppointmentForm()
    if request.method == 'POST':
        appt_form = AppointmentForm(request.POST)
        if appt_form.is_valid():
            appointment = appt_form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'New Appointment Created'
            )
            return redirect('index')

    return render(request, 'appt/create_appt.html', {'appt_form': appt_form})



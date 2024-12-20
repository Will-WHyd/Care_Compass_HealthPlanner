from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Appointment, Consultant
from user_profile.models import Profile
from .forms import AppointmentForm, ConsultantForm


# Create your views here.
class ApptList(generic.ListView):
    """
    Displays list of appointments belonging to the logged-in user.

    List is displayed in decending order of 'appt_date'.
    """
    model = Appointment
    template_name = 'appt/index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Appointment.objects.filter(user=self.request.user).order_by('-appt_date')
        else:
            return Appointment.objects.none()
    paginate_by = 12


@login_required
def appt_detail(request, id):
    """
    Displays appointment details page for selected appointment.

    **Context**
    ``appt``
        An instance of :model:`med_appt.Appointment`
    """
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
    """
    Creates a new instance of Appointment via form.
    """
    appt_form = AppointmentForm()
    if request.method == 'POST':
        appt_form = AppointmentForm(request.POST, user=request.user)
        if appt_form.is_valid():
            appointment = appt_form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'New Appointment Created'
            )
            return redirect('appointments:detail', appointment.id)

    return render(request, 'appt/create_appt.html', {'appt_form': appt_form})


@login_required
def appt_edit(request, id):
    """
    Redirects from an appointment detail page to a form page
    which allows editing and updating of appointment details.

    **Context**
    ``appt``
        An instance of :model:`med_appt.Appointment`
    """
    appt = get_object_or_404(Appointment, id=id)

    if appt.user != request.user:
        return render(request, "appt/403.html")

    if request.method == 'POST':
        appt_form = AppointmentForm(request.POST, instance=appt)
        if appt_form.is_valid():
            appt_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Appointment Details Updated'
            )
            return redirect('appointments:detail', id=appt.id)
    else:
        appt_form = AppointmentForm(instance=appt)

    return render(request, 'appt/edit_appt.html', {'appt_form': appt_form, 'appt': appt})


@login_required
def appt_delete(request, id):
    """
    Redirects from an appointment detail page to delete that appointment.

    **Context**
    ``appt``
        An instance of :model:`med_appt.Appointment`
    """
    appt = get_object_or_404(Appointment, id=id)

    if appt.user == request.user:
        appt.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Appointment Deleted!'
            )
        return redirect('appointments:home')
    else:
        return render(request, "appt/403.html")


@login_required
def consultant_create(request):
    """
    Creates a new instance of Consultant via form.
    """
    form = ConsultantForm()
    if request.method == 'POST':
        form = ConsultantForm(request.POST)
        if form.is_valid():
            consultant = form.save(commit=False)
            consultant.user = request.user
            consultant.save()
            # Adds user profile to new consultant's 'clients' field.
            consultant.clients.add(request.user.profile)
            consultant.save()
            messages.add_message(
                request, messages.SUCCESS,
                'New Consultant Created'
            )
            return redirect('profile:profile')

    return render(request, 'appt/create_consultant.html', {'form': form})


@login_required
def consultant_edit(request, id):
    """
    Redirects from a displayed consultant card on profile page
    to a form page which allows editing and updating of Consultant details.

    **Context**
    ``consultant``
        An instance of :model:`med_appt.Consultant`
    """
    consultant = get_object_or_404(Consultant, id=id)

    if consultant.user != request.user:
        return render(request, "appt/403.html")

    if request.method == 'POST':
        form = ConsultantForm(request.POST, instance=consultant)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Consultant Details Updated'
            )
            return redirect('profile:profile')
    else:
        form = ConsultantForm(instance=consultant)

    return render(request, 'appt/edit_consultant.html', {'form': form, 'consultant': consultant})


@login_required
def consultant_delete(request, id):
    """
    Redirects from a displayed consultant card
    on profile page to delete that Consultant.

    **Context**
    ``consultant``
        An instance of :model:`med_appt.Consultant`
    """
    consultant = get_object_or_404(Consultant, id=id)

    if consultant.user == request.user:
        consultant.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Consultant Deleted!'
            )
        return redirect('profile:profile')
    else:
        return render(request, "appt/403.html")

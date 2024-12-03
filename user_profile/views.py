from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import Profile

# Create your views here.

def profile_view(request):
    """
    Renders the most recent information on the user's profile page.
    Displays an individual instance of :model: 'user_profile.Profile'
    """

    profile = get_object_or_404(Profile.objects.filter(user=request.user).order_by('-updated_on'))

    return render(request, "profile/profile.html", {"profile": profile})

@login_required
def edit_profile(request):
    """
    Renders the profile settings edit page
    """
    template = "edit_profile.html"
    profile = get_object_or_404(Profile.objects.filter(user=request.user).order_by('-updated_on'))
    profile_form = ProfileForm()
     
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Profile Details Updated'
                )
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=profile)
        
    return render(request, 'profile/edit_profile.html', {'profile_form': profile_form, 'profile': profile})

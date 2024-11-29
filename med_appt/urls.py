from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.ApptList.as_view(), name='home'),
    ]
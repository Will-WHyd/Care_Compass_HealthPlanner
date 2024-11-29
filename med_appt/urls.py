from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.ApptList.as_view(), name='home'),
    path('<id>/', views.appt_detail, name='appt_detail'),
    ]
from . import views
from django.urls import path, include

urlpatterns = [
    path('create/', views.appt_create, name='create_appt'),
    path('', views.ApptList.as_view(), name='home'),
    path('<id>/', views.appt_detail, name='appt_detail'),
    ]
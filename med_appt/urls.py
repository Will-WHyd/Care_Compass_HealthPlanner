from . import views
from django.urls import path, include

app_name = 'appointments'

urlpatterns = [
    path('appointments/create/', views.appt_create, name='create'),
    path('appointments/<id>/', views.appt_detail, name='detail'),
    path('appointments/<id>/edit/', views.appt_edit, name='edit'),
    path('appointments/<id>/delete/', views.appt_delete, name='delete'),
    path('consultants/', views.ConsultList.as_view(), name='consultants'),
    path('consultant/create/', views.consultant_create, name='consultant_create'),
    path('consultant/<id>/edit/', views.consultant_edit, name='consultant_edit'),
    path('consultant/<id>/delete/', views.consultant_delete, name='consultant_delete'),
    path('', views.ApptList.as_view(), name='home'),
    ]
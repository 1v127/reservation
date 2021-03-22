from django.urls import path
from . import views

app_name='doctor'

urlpatterns=[
    path('', views.doctor_resume(), name='doctor_resome'),
]
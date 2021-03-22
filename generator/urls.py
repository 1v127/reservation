from django.urls import path
from . import views

app_name='guest'

urlpatterns=[
    path('', views.guest_resume(), name='guest_resome'),
]
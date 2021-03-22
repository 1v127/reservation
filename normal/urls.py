from django.urls import path
from . import views

app_name='normal'

urlpatterns=[
    path('', views.index, name='index'),
]
from django.urls import path
from . import views

# Path del core

urlpatterns = [
    path('', views.contact, name='contact'),
]
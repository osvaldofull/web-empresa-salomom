from django.urls import path
from core import views

# Path del core

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
]
from django.urls import path
from . import views

# Path del core

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:category_id>/', views.category, name="category"),
]
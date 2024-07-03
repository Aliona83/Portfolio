# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_me/', views.about_me, name='about_me'),
    path('projects/', views.about_me, name='projects'),
    path('contact_me/', views.about_me, name='contact_me'),
    # Add other URL patterns as needed
]

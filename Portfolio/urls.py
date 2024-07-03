# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    # path('home/', views.home, name='home'),
    path('about_me/', views.about_me, name='about_me'),
    path('projects/', views.projects, name='projects'),
    path('contact_me/', views.contact_me, name='contact_me'),
    # Add other URL patterns as needed
]

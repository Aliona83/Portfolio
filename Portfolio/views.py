from django.shortcuts import render
from .models import About_me, Experience

from django.shortcuts import render

def base(request):
    return render(request, 'Portfolio/base.html')

def main(request):
    return render(request, 'Portfolio/main.html')

def about_me(request):
    about_me = About_me.objects.first()
    experiences = Experience.objects.all()
    context = {
        'title': about_me.title,
        'description': about_me.description,
        'experiences': experiences,}
    return render(request, 'Portfolio/about_me.html',context)

def projects(request):
    return render(request, 'Portfolio/projects.html')

def contact_me(request):
    return render(request, 'Portfolio/contact_me.html')

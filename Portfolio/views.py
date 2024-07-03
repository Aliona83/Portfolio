from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render

def index(request):
    return render(request, 'Portfolio/index.html')
def about_me(request):
    return render(request, 'Portfolio/about_me.html')
def projects(request):
    return render(request, 'Portfolio/projects.html')

def contact_me(request):
    return render(request, 'Portfolio/contact_me.html')

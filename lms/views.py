from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def entry_views(request):
    if request.user.is_authenticated:
        return render(request, 'home-page.html', {})    
    else:
        return render(request, 'landing-page.html', {})
     
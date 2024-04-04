"""
Defines views for the 'lms' app.
"""

from django.shortcuts import render

def entry_views(request):
    """
    Renders home/landing based on whether the user is authenticated.
    """
    if request.user.is_authenticated:
        return render(request, 'home-page.html', {})
    return render(request, 'landing-page.html', {})
     
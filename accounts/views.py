"""
Module: Defines views for the 'accounts' app.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


@login_required
def home(request):
    # Renders the home page if the user is authenticated
    return render(request, 'home-page.html', {})


def entry_view(request):
    # Decides which page to render (home / landing) based on whether the user is authenticated or not
    if request.user.is_authenticated:
        return render(request, 'home-page.html', {})
    else:
        return render(request, 'landing-page.html', {})


def authentication_view(request):
    # Authentication view for registration of new users
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            if 'adminUserCheckbox' in request.POST:
                user.is_staff = True
            user.save()
            return redirect('/login')
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    # Login view for existing users
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error_message = 'Invalid username or password'
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    # Logout view for existing users
    logout(request)
    return redirect('home')

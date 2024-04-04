"""
Module: URLs configuration for 'accounts' app.
"""

from django.urls import path, include
from .views import authentication_view, login_view, logout_view, entry_view

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authentication_view, name="authenticationView"),
    path("", entry_view, name="home"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]


from django.urls import path,include
from .views import authenticationView, home,login_view,logout_view, entry_view;

urlpatterns = [
  path("accounts/", include("django.contrib.auth.urls")),
  path("signup/", authenticationView, name="authenticationView"),   
  path("", entry_view, name="home"), 
  path('login/', login_view, name='login'),
  path('logout/',logout_view, name='logout'),
]

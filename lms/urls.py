"""
URL configuration for team_talk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import entry_views
from pages.views import createExam, Examlist, create_exam, exam, add_question, results, studentExamList,examination, submit_exam,update_exam, myResults
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(("accounts.urls","signupLogin"),"signupLogin")),
    path('', entry_views, name='home'),
    path('createExam/', createExam, name='createExam'),
    path('Examlist/', Examlist, name='Examlist'),
    path('exam/<int:id>/', exam, name='exam'),
    path('results/<int:id>/', results,name='results'),
    path('openExam/', studentExamList ,name='studentExamList'),
    path('examination/<int:id>/', examination ,name='examination'),
    path('myResults', myResults ,name='myResults'),

    path('create_exam/', create_exam, name='create_exam'),    
    path('add_question/<int:exam_id>/',add_question, name='add_question'),
    path('submit_exam/<int:exam_id>/', submit_exam, name='submit_exam'),
    path('update_exam/<int:exam_id>/', update_exam, name='update_exam'),

]   

"""
Module: URLs configuration for 'lms' app.
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import (
    create_exam, exam_list, create_exam_teacher, exam,
    add_question, results, student_exam_list,
    examination, submit_exam, update_exam,
    my_results
)

from .views import entry_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(("accounts.urls", "signupLogin"), "signupLogin")),
    path('', entry_views, name='home'),
    path('createExam/', create_exam_teacher, name='createExam'),
    path('Examlist/', exam_list, name='Examlist'),
    path('exam/<int:exam_id>/', exam, name='exam'),
    path('results/<int:exam_id>/', results, name='results'),
    path('openExam/', student_exam_list, name='studentExamList'),
    path('examination/<int:exam_id>/', examination, name='examination'),
    path('myResults/', my_results, name='myResults'),

    path('create_exam/', create_exam, name='create_exam'),
    path('add_question/<int:exam_id>/', add_question, name='add_question'),
    path('submit_exam/<int:exam_id>/', submit_exam, name='submit_exam'),
    path('update_exam/<int:exam_id>/', update_exam, name='update_exam'),
]

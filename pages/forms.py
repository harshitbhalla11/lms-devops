"""
Forms for pages app which includes exam form
"""
from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'description', 'duration', 'visibility']

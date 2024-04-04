"""
    forms.py
"""
from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):
    """
    Exam form
    """

    class Meta:
        """
        exam form fields
        """
        model = Exam
        fields = ['title', 'description', 'duration', 'visibility']

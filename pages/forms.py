"""
    forms.py
"""
from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):
    """
    Exam form
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        """
        exam form fields
        """
        model = Exam
        fields = ['title', 'description', 'duration', 'visibility']

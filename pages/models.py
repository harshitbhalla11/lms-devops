from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Exam(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exams')
    visibility = models.BooleanField(default=False)

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    options = models.TextField()  
    correct_answer = models.PositiveSmallIntegerField()
    marks = models.PositiveSmallIntegerField(default=1)

class QuizAttempt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_attempts')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    submission_time = models.DateTimeField(auto_now_add=True)
    total_questions = models.PositiveIntegerField()
    correct_answers = models.PositiveIntegerField()
    score = models.PositiveIntegerField()




    

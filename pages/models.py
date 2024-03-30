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
    question= models.CharField(default ='', max_length=50)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_answer = models.IntegerField()
    marks = models.IntegerField(default=1)


class QuizAttempt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_attempts')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    submission_time = models.DateTimeField(auto_now_add=True)
    total_questions = models.PositiveIntegerField()
    correct_answers = models.PositiveIntegerField()
    score = models.PositiveIntegerField()
    max_marks= models.PositiveIntegerField()




    

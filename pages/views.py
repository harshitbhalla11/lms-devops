from django.shortcuts import render

def createQuiz(request):
    return render(request, 'create-quiz.html', {})
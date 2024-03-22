from django.shortcuts import render

def createExam(request):
    return render(request, 'createExam.html', {})





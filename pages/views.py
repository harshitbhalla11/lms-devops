from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Exam
def createExam(request):
    return render(request, 'teacher/createExam.html', {})

def Examlist(request):
    exams = Exam.objects.all() 
    return render(request, 'teacher/Examlist.html', {'exams': exams})

@login_required
def create_exam(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        teacher_id = request.user.id
        visibility = request.POST.get('visibility') == 'on'  

        exam = Exam.objects.create(
            title=title,
            description=description,
            duration=duration,
            teacher_id=teacher_id,
            visibility=visibility
        )
        
        return redirect('Examlist')  

    return render(request, 'create_exam.html')
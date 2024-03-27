from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Exam, Question, QuizAttempt
from django.http import HttpResponse

def createExam(request):
    return render(request, 'teacher/createExam.html', {})

def Examlist(request):
    exams = Exam.objects.all() 
    return render(request, 'teacher/Examlist.html', {'exams': exams})


def exam(request, id):
    exam = Exam.objects.get(id=id)
    questions= Question.objects.filter(exam_id=id)
    return render(request, 'teacher/exam.html', {'exam': exam, 'questions': questions})

def results(request,id):
    results= QuizAttempt.objects.filter(exam_id=id)
    return render (request,'teacher/results.html',{'results':results})


# student views 
def examination(request,id):
    exam = Exam.objects.get(id=id)
    questions=Question.objects.filter(exam_id=id)
    return render (request,'student/examination.html', {'exam':exam, 'questions':questions})

def studentExamList(request):
    exams = Exam.objects.filter(visibility=True) 
    return render(request, 'student/studentExamlist.html', {'exams': exams})

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


def add_question(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    if request.method == 'POST':
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correct_answer = int(request.POST.get('correct'))
        marks = int(request.POST.get('marks'))
        question=request.POST.get('question')

        question = Question.objects.create(
            exam=exam,
            question=question,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            correct_answer=correct_answer,
            marks=marks
        )
        return redirect('exam', id=exam_id) 

    return redirect('exam', id=exam_id) 



def submit_exam(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)

    if request.method == 'POST':
        student = request.user
        exam_id = request.POST.get('exam_id')
        total_questions = 0
        correct_answers = 0
        total_marks = 0
        
        for question in exam.questions.all():

            if f'question_{question.id}' in request.POST:
                total_questions += 1
                
                if request.POST.get(f'question_{question.id}') == str(question.correct_answer):
                    correct_answers += 1
                    total_marks += question.marks
        
        quiz_attempt = QuizAttempt.objects.create(
            student=student,
            exam=exam,
            total_questions=total_questions,
            correct_answers=correct_answers,
            score=total_marks 
        )
        return redirect('studentExamList')  
    else:
        return HttpResponse(status=405)

from django.shortcuts import redirect
from .models import Exam

def update_exam(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        visibility = request.POST.get('visibility') == 'on'
        
        exam.title = title
        exam.description = description
        exam.duration = duration
        exam.visibility = visibility
        
        exam.save()
        
        return redirect('exam', id=exam_id) 

    return redirect('exam', id=exam_id) 


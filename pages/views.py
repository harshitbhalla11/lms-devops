"""
Module: Defines views for 'pages' app.
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Exam, Question, QuizAttempt
from .forms import ExamForm




def create_exam_teacher(request):
    """
    Create exam view for teachers.
    """
    return render(request, 'teacher/createExam.html', {})

def exam_list(request):
    """
    Create exam list view for teachers.
    """
    exams = Exam.objects.all()
    return render(request, 'teacher/Examlist.html', {'exams': exams})


def exam(request, exam_id):
    """
    Create exam edit page for teachers.
    """
    exam_data = Exam.objects.get(id=exam_id)
    questions= Question.objects.filter(exam_id=exam_id)
    return render(request, 'teacher/exam.html', {'exam': exam_data, 'questions': questions})

def results(request, exam_id):
    """
    Show exam result view for teachers which supports student search
    """
    results_data = QuizAttempt.objects.filter(exam_id=exam_id)
    
    search_query = request.GET.get('searchedName')
    if search_query:
        results_data = results_data.filter(student__username__icontains=search_query)
    
    return render(request, 'teacher/results.html', {'results': results_data})



# student views
def examination(request,exam_id):
    """
    Create exam view for students.
    """
    exam_data = Exam.objects.get(id=exam_id)
    questions=Question.objects.filter(exam_id=exam_id)
    return render (request,'student/examination.html', {'exam':exam_data, 'questions':questions})

def student_exam_list(request):
    """
    Create examList view for students.
    """
    exams_data = Exam.objects.filter(visibility=True)
    return render(request, 'student/studentExamList.html', {'exams': exams_data})

# return current student results
def my_results(request):
    """
    Create my result view for students.
    """
    results_data = QuizAttempt.objects.filter(student=request.user)
    return render(request, 'student/myResults.html', {'results': results_data})

@login_required
def create_exam(request):
    """
    store exam view for teacher.
    """
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam_form = form.save(commit=False)
            exam_form.teacher = request.user
            exam_form.save()
            return redirect('Examlist')
    else:
        form = ExamForm()
    return render(request, 'teacher/createExam.html', {'form': form})

def add_question(request, exam_id):
    """
    store question view for teacher.
    """
    exam_data = Exam.objects.get(id=exam_id)
    if request.method == 'POST':
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correct_answer = int(request.POST.get('correct'))
        marks = int(request.POST.get('marks'))
        question=request.POST.get('question')

        question = Question.objects.create(
            exam=exam_data,
            question=question,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            correct_answer=correct_answer,
            marks=marks
        )
        return redirect('exam', exam_id=exam_id)

    return redirect('exam', exam_id=exam_id)


def submit_exam(request, exam_id):
    """
    submit exam view for student.
    score calculation and store in database.
    """
    exam_data= Exam.objects.get(pk=exam_id)

    if request.method == 'POST':
        student = request.user
        exam_id = request.POST.get('exam_id')
        total_questions = 0
        correct_answers = 0
        total_marks = 0

        for question in exam_data.questions.all():

            if f'question_{question.id}' in request.POST:
                total_questions += 1

                if request.POST.get(f'question_{question.id}') == str(question.correct_answer):
                    correct_answers += 1
                    total_marks += question.marks

        max_marks = exam_data.questions.aggregate(total_marks=Sum('marks'))['total_marks']

        QuizAttempt.objects.create(
            student=student,
            exam=exam_data,
            total_questions=total_questions,
            correct_answers=correct_answers,
            score=total_marks ,
            max_marks=max_marks
        )
        return redirect('myResults')
    return HttpResponse(status=405)

def update_exam(request, exam_id):
    """
    Update exam view for teacher.
    """
    exam_data = Exam.objects.get(id=exam_id)
    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        visibility = request.POST.get('visibility') == 'on'

        exam_data.title = title
        exam_data.description = description
        exam_data.duration = duration
        exam_data.visibility = visibility

        exam_data.save()

        return redirect('exam', exam_id=exam_id)

    return redirect('exam', exam_id=exam_id)

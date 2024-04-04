from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Complaints, Forum, Marks, Student
from .forms import CommentForm, ForumForm, MarksForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import *
# def registration_view(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             return render(request, 'details.html', {'data': data})
#     else:
#         form = RegistrationForm()
#     return render(request, 'registration_form.html', {'form': form})

def login_view(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print("partially success" + "\n\n")
        if user is not None:
             print("success")
             login(request, user)
             return redirect(view_home)
    return render(request, 'login.html') 

def view_home(request):
    student_name = request.user.username
    return render(request, 'home.html',{'student_name' : student_name})


def forum_view(request):
    if(request.method == 'POST'):
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('error')
        return redirect(forum_view)
    else:
        forums = Forum.objects.all()
        form = ForumForm()
        return render(request, 'forum.html', {'forums': forums, 'form' : form})

def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'forum_list.html', {'forums' : forums})

def forum_details(request, forum_id):
     print("title reached to function " +   str(forum_id))
     forum = get_object_or_404(Forum, pk=forum_id)
     form = CommentForm()
     return render(request, 'forum_details.html', {'forum' : forum , 'form' : form})


def submit_comment(request, forum_id):
    forum = Forum.objects.get(pk=forum_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.cleaned_data['new_comment']
            forum.add_comment(new_comment)
            return redirect('forum-details', forum_id=forum_id )
        
    return redirect('forum-details', forum_id=forum_id)


# def article_view(request):
#     articles = Article.objects.all()
#     print(articles)
#     return render(request, 'article.html', {'articles' : articles})

def add_marks(request):
    students = Student.objects.all()
    if request.method == 'POST':
        for student in students:
            marks_value = request.POST.get(f"marks_{student.id}")
            if marks_value is not None:
                # Convert the input data to a floating-point number
                marks_value_float = float(marks_value)
                marks, created = Marks.objects.get_or_create(student=student)
                marks.cgp = marks_value_float  # Assign the floating-point value
                marks.save()
        return redirect('add-marks')
    return render(request, 'add_marks.html', {'students': students})

def view_marks(request):
    marks_details = Marks.objects.all()
    return render(request, 'view_marks.html', {'marks_details' : marks_details})

def add_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum-list')
    else:
        form = ForumForm()
    return render(request, 'add_forum.html', {'form': form})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # semester = request.POST.get('semester')
            # batch = request.POST.get('batchNo')
            # batchId = f"{batch}{semester}"
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            student = Student(name=name, description=description)
            student.save()

            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def view_student(request):
    student_details = Student.objects.all()
    return render(request, 'view_student.html', {'students' : student_details})


def add_complaint(request):
    if request.method == 'POST':
        print('working till here\n\n\n')
        subject = request.POST.get('subject')
        complaint_text = request.POST.get('complaintText')
        complaint = Complaints(subject=subject, description=complaint_text)
        complaint.save()
        return redirect('add-complaint')
    all_complaints = Complaints.objects.all()
    return render(request, 'complaintforum.html', {'complaints' : all_complaints})

def complaint_details(request, complaint_id):
    print(complaint_id)
    return render(request, 'complaintdetails.html')

def delete_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaints, pk=complaint_id)
    complaint.delete()
    return redirect('add-complaint') 
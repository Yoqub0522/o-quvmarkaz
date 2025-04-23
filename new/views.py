from django.shortcuts import render, redirect

from .forms import CourseForm, StudentForm
from .models import Course, Student


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course-list')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

def student_list(request):
    courses = Student.objects.all()
    return render(request, 'student_list.html', {'courses': courses})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def get_student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    context={
        'student':student
    }
    return render(request, 'student_detail.html', {'student':student})

def student_update(request, pk):
    student=Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'create_student.html', {'form': form})


def delete_student(request,pk):
    student=Student.objects.get(pk=pk)
    if request.method=='POST':
        student.delete()
        return redirect('student-list')
    return render(request,'delete_student.html',{'student':student})

def get_course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    context={
        'course':course
    }
    return render(request, 'course_detail.html', {'course':course})


def course_update(request, pk):
    course=Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course-list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'create_course.html', {'form': form})


def delete_course(request,pk):
    course=Course.objects.get(pk=pk)
    if request.method=='POST':
        course.delete()
        return redirect('course-list')
    return render(request,'delete_course.html',{'course':course})







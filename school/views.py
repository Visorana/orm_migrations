from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.prefetch_related('teachers').order_by('name')
    for student in students:
        print(student.teachers.all())
    context = {'students': students}
    return render(request, template, context)

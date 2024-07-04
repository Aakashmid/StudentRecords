from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,UpdateView,CreateView,DeleteView,DetailView
from .models import Student
# Create your views here.
# Using Class Based View

class StudentList(ListView):
    model=Student
    queryset=Student.objects.all()
    template_name='studentApp/index.html'
    context_object_name='students'


class StudentDetail(DetailView):
    model=Student
    template_name='studentApp/studetail.html'
    context_object_name='student'
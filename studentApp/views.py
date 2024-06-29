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

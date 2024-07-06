from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,UpdateView,CreateView,DeleteView,DetailView
from .models import Student
from django.db.models import Q
from django.urls import reverse_lazy
# Create your views here.
# Using Class Based View

class StudentList(ListView):
    model=Student
    queryset=Student.objects.all()
    template_name='studentApp/index.html'
    context_object_name='students'

    def get_queryset(self):
        queryset= super().get_queryset()  # init queryset
        query=self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query) )
        return queryset
    

class StudentDetail(DetailView):
    model=Student
    context_object_name='student'
    template_name='studentApp/studetail.html'

# class StudentCreate(CreateView):
#     pass

# class StudentUpdate(UpdateView):
#     pass

class StudentDelete(DeleteView):
    model=Student
    success_url=reverse_lazy('StuApp:student-list')

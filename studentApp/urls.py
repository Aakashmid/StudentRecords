from django.urls import path,include
from studentApp import views

urlpatterns = [
    path('',views.StudentList.as_view(),name='student-list')
]

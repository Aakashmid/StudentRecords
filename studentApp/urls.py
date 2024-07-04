from django.urls import path,include
from studentApp import views
app_name="StuApp"

urlpatterns = [
    path('',views.StudentList.as_view(),name='student-list'),
    path('student/<int:pk>',views.StudentDetail.as_view(),name='Student-Detail')
]

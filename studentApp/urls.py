from django.urls import path,include
from studentApp import views
app_name="StuApp"

urlpatterns = [
    path('',views.StudentList.as_view(),name='student-list'),
    path('add-student/',views.StudentCreate.as_view(),name='Student-Create'),
    path('detail/<int:pk>',views.StudentDetail.as_view(),name='Student-Detail'),
    path('delete/<int:pk>',views.StudentDelete.as_view(),name='Student-Delete')
]

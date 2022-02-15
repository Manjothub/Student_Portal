from django.urls import path
from HOD .views import *

urlpatterns = [
    path('home',hodpage,name="hodpage"),
    path('student/add',addstudents,name="addstudent"),
    path('student/view',viewstudents,name="viewstudent"),
    path('student/edit/<str:id>',editstudents,name="editstudent"),
    path('student/update/',updatestudents,name="updatestudent")
]

from django.urls import path
from HOD .views import *

urlpatterns = [
    path('home',hodpage,name="hodpage"),
    path('student/add',addstudents,name="addstudent"),
    path('student/view',viewstudents,name="viewstudent"),
    path('student/edit/<str:id>',editstudents,name="editstudent"),
    path('student/update/',updatestudents,name="updatestudent"),
    path('student/delete/<str:id>',deletestudents,name="deletestudent"),
    
    path('course/add',addcourse, name="addcourse"),
    path('course/view',viewcourses, name="viewcourse"),
    path('course/edit/<str:id>',editcourses,name="editcourse"),
    path('course/update/',updatecourses,name="updatecourse"),
    path('course/delete/<str:id>',deletecourses,name="deletecourse"),
    
    path('teacher/add',addTeacher,name="addTeacher")
    
]

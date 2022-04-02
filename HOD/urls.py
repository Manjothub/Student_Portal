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
    
    path('teacher/add',addTeacher,name="addTeacher"),
    path('teacher/view',viewTeacher,name="viewTeacher"),
    path('teacher/edit/<str:id>',editTeacher,name="editTeacher"),
    path('teacher/update/',updateTeacher,name="updateTeacher"),
    path('teacher/delete/<str:id>',deleteTeacher,name="deleteTeacher"),
    
    path('subject/add',addSubject,name="addSubject"),
    path('subject/view',viewSubject,name="viewSubject"),
    path('subject/edit/<str:id>',editSubject,name="editSubject"),
    path('subject/update/',updateSubject,name="updateSubject"),
    path('subject/delete/<str:id>',deleteSubject,name="deleteSubject"),
    
    path('session/add',addSession,name="addSession"),
    path('session/view',viewSession,name="viewSession"),
    path('session/edit/<str:id>',editSession,name="editSession"),
    path('session/update',updateSession,name="updateSession"),
    path('session/delete/<str:id>',deleteSession,name="deleteSession"),
    
    path("staff/send/notification",staffsendnotification,name="sendnotification"),
    path("staff/save/notification",staffsavenotification,name="savestaffnotification"),
    path('staff/leave/view',staffleaveview,name="leaveview"),
    path('staff/leave/approve/<str:id>',staffapproveleave,name="leaveapprove"),
    path('staff/leave/disapprove/<str:id>',staffdisapproveleave,name="leavedisapprove"),
    path('staff/feedback/',stafffeedback,name="stafffeedbackreply"),
    path('staff/send/feedback/',staffsendfeedback,name="sendreply"),
    
    path('student/send-notification',studentsendnotification,name="studentsendnotification"),
    path('student/save/notification',studentsavenotification,name="savestudentnotification"),
    path('student/leave/view',studentviewleave,name="studentviewleave"),
    path('student/leave/approve/<str:id>',studentapproveleave,name="studentleaveapprove"),
    path('student/leave/disapprove/<str:id>',studentdisapproveleave,name="studentleavedisapprove"),
    path('student/feedback/',studentfeedback,name="studentfeedbackreply"),
    path('student/send/feedback/',studentsendfeedback,name="studentsendreply"),
    path('student/view/attendance',viewattendance,name="viewattendance")
    
    
]

from django.urls import path
from Student .views import *

urlpatterns = [
    path('home',studenthome,name="studenthome"),
    path('notification/',studentnotification,name="studentnotification"),
    path('notification/mark-as-done/<str:id>',studentnotifydone,name="studentnotifystatus"),
    path('feedback',studentfeedback,name="studentfeedbacks"),
    path('feedback/save',studentsavefeedback,name="studentfeedbacksave"),
    path('student/leave/view',studentleaveview,name="studentleaveview"),
    path('student/add/leave',studentsendleave,name="studentleave")
]


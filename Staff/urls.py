from django.urls import path
from Staff .views import *

urlpatterns = [
    path('home',staffpage,name="staffpage"),
    path('staff/notification',staffnotification,name="notification"),
    path('staff/mark-as-done/<str:id>',staffnotifydone,name="staffnotifystatus"),
    
    path('staff/apply-leave',staffapplyleave,name="staffapplyleave"),
    path('staff/add/leave',staffsendleave,name="sendleave")
]

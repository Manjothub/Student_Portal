from django.urls import path
from HOD .views import *

urlpatterns = [
    path('home/',hodpage,name="hodpage")
]

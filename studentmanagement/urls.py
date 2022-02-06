from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import *
from HOD.views import *
from Staff.views import *
from Student.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #login page url
    path('',loginpage, name="loginpage"),
    
    #login form route url
    path('doLogin/',doLogin,name='doLogin'),
    path('doLogout',doLogout,name='doLogout'),
    
    #Profile Page
    path('profile/',profile,name="profile"),
    path('profile-update',profileupdate,name="profileupdate"),
    
    #HOD Pannel url
    path('/Hod/',include('HOD.urls')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

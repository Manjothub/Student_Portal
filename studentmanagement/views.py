from django.shortcuts import render,redirect,HttpResponse
from app.emailbackend import Emailbackend
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from app.models import *


def loginpage(request):
    return render(request,'main/login.html')


def doLogin(request):
    if request.method == 'POST':
        user = Emailbackend.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            user_type=user.user_type
            if user_type == '1':
                return redirect('hodpage')
            elif user_type =='2':
                return HttpResponse('This is Staff Pannel')
            elif user_type =='3':
                return HttpResponse('This is Student Pannel')
            else:
                messages.error(request,"Invalid Credentials")
                return redirect('loginpage')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('loginpage')
        
        
def doLogout(request):
    logout(request)
    return redirect('loginpage')


def profile(request):
    user=Customuser.objects.get(id=request.user.id)
    context={
        "user":user
    }
    return render(request, 'main/profile.html',context)

def profileupdate(request):
    if request.method == 'POST':
        profile_pic=request.FILES.get("profile_pic")
        first_name=request.POST.get("firstname")
        last_name=request.POST.get("lastname")
        # email=request.POST.get("email")
        # username=request.POST.get("username")
        password=request.POST.get("password")
        
        try:
            customUser=Customuser.objects.get(id=request.user.id)
            customUser.first_name=first_name
            customUser.last_name=last_name
            customUser.profile_pic=profile_pic
            if password == None and password == '':
                customUser.set_password(password)
            customUser.save()
            messages.success(request,"Your Profile Updated Successfully")
            redirect("profileupdate")
            print(profile_pic)
            
        except:
            messages.error(request,"Fail to update your Profile")
    return render(request,'main/profile.html')
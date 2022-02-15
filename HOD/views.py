from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app .models import *


@login_required(login_url="/")
def hodpage(request):
    return render(request,'HOD/home.html')

@login_required(login_url="/")
def addstudents(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')
        birth_date = request.POST.get('DOB_student')
        gender =request.POST.get('gender')
        course = request.POST.get('course_id')
        session = request.POST.get('session_year_id')
        profile = request.FILES.get('profile_pic')
        mobile_no = request.POST.get('student_mobile')
        mobile_no_optional = request.POST.get('student_optional_mobile')
        permanent_address= request.POST.get('permanent_address')
        present_address= request.POST.get('present_address')
        
        # print(first_name,last_name,email,username,password,DOB,gender,course,session,profile,mobile_no,mobile_no_optional,permanent_address,present_address)
        if Customuser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already Taken')
            return redirect('addstudent')
        if Customuser.objects.filter(username=username).exists():
            messages.warning(request,username + 'Already Taken')
            return redirect('addstudent')
        else:
            user= Customuser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile,
                user_type=3
            )    
            user.set_password(password)
            user.save()
            course = Course.objects.get(id= course)
            session =Session_Year.objects.get(id=session)
            students= Student(
                admin=user,
                student_dob =birth_date,
                permanent_address=permanent_address,
                present_address=present_address,
                gender =gender,
                student_mobile_no =mobile_no,
                student_optional_mobile_no =mobile_no_optional,
                course_id =course,
                session_id =session,
            )
            students.save()
            messages.success(request,user.first_name + "  " + user.last_name + '  successfully Saved')
            return redirect('addstudent')
    course= Course.objects.all()
    session_year = Session_Year.objects.all()
    context = {
        'course' :course,
        'session_year': session_year,
    }
    return render(request,'HOD/add_student.html',context)


def viewstudents(request):
    students=Student.objects.all()
    return render(request,'HOD/view_student.html',{'students':students})


def editstudents(request,id):
    student=Student.objects.filter(id=id)
    course=Course.objects.all()
    session =Session_Year.objects.all()
    context ={
        'students':student,
        'course':course,
        'session':session
    }    
    return render(request,'HOD/edit_student.html',context)

def updatestudents(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')
        birth_date = request.POST.get('DOB_student')
        gender =request.POST.get('gender')
        course = request.POST.get('course_id')
        session = request.POST.get('session_year_id')
        profile = request.FILES.get('profile_pic')
        mobile_no = request.POST.get('student_mobile')
        mobile_no_optional = request.POST.get('student_optional_mobile')
        permanent_address= request.POST.get('permanent_address')
        present_address= request.POST.get('present_address')
        
    return render(request,'HOD/edit_student.html')
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

@login_required(login_url="/")
def viewstudents(request):
    students=Student.objects.all()
    return render(request,'HOD/view_student.html',{'students':students})

@login_required(login_url="/")
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

@login_required(login_url="/")
def updatestudents(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')
        birth_date = request.POST.get('student_dob')
        gender =request.POST.get('gender')
        course = request.POST.get('course_id')
        session = request.POST.get('session_id')
        profile = request.FILES.get('profile_pic')
        mobile_no = request.POST.get('student_mobile_no')
        mobile_no_optional = request.POST.get('student_optional_mobile_no')
        permanent_address= request.POST.get('permanent_address')
        present_address= request.POST.get('present_address')
        
        user = Customuser.objects.get(id = student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != None and password != "":
            user.set_password(password)
        if profile != None and profile != "":
            user.profile_pic =profile
        user.save()
        
        student=Student.objects.get(admin = student_id)
        student.student_dob = birth_date
        student.gender = gender
        student.student_mobile_no = mobile_no
        student.student_optional_mobile_no =mobile_no_optional
        student.permanent_address = permanent_address
        student.present_address = present_address
        course=Course.objects.get(id = course)
        student.course_id = course
        session_year = Session_Year.objects.get(id = session)   
        student.session_id = session_year
        student.save()
        messages.success(request,'Record Successfully Updated !')     
        return redirect('viewstudent')
    return render(request,'HOD/edit_student.html')

@login_required(login_url="/")
def deletestudents(request,id):
    student= Student.objects.get(id=id)
    student.delete()
    return redirect('viewstudent')



@login_required(login_url="/")
def addcourse(request):
    if request.method == 'POST':
        course_name=request.POST.get('course_name')
        course = Course(
            name= course_name
        )
        if course:
            course.save()
            messages.success(request,'Course Added Sucessfully')
        else:
            messages.error(request,'Something went wrong')   
    return render(request,'HOD/add_course.html')

@login_required(login_url="/")
def viewcourses(request):
    course=Course.objects.all()
    context = {
        'courses':course
    }
    return render(request,'HOD/view_course.html',context)

@login_required(login_url="/")
def editcourses(request,id):
    courses=Course.objects.filter(id=id)
    context={
        'courses':courses
    }
    return render(request,'HOD/edit_course.html',context)

def updatecourses(request):
    if request.method == 'POST':
        course_name=request.POST.get('name')
        course=Course(name=course_name)
        if course:
            course.save()
            messages.success(request,'Course Updated !')
            return redirect('viewcourse')
        
    return render(request,'HOD/edit_course.html')


@login_required(login_url="/")
def deletecourses(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect('viewcourse')


@login_required(login_url="/")
def addTeacher(request):
    return render(request,'HOD/add_teacher.html')
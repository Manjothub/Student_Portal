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
    if request.method == 'POST':
        profile = request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')   
        birth_date = request.POST.get('dob_teacher')
        mobile = request.POST.get('mobile')
        gender =request.POST.get('gender') 
        joining_date = request.POST.get('join_date')
        qualification = request.POST.get('qualification')
        experience=  request.POST.get('experience')
        address = request.POST.get('address')
        if Customuser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already Taken')
            return redirect('addTeacher')
        if Customuser.objects.filter(username=username).exists():
            messages.warning(request,username + 'Already Taken')
            return redirect('addTeacher')
        else:
            user= Customuser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile,
                user_type=2
            )    
            user.set_password(password)
            user.save()
            teacher= Staff(
                admin=user,
                staff_dob =birth_date,
                staff_gender =gender,
                staff_mobile_no =mobile,
                staff_joining_date = joining_date,
                staff_qualification = qualification,
                staff_experience = experience,
                staff_address =address
            )
            teacher.save()
            messages.success(request,user.first_name + "  " + user.last_name + '  successfully Saved')
            return redirect('addTeacher')
    return render(request,'HOD/add_teacher.html')

def viewTeacher(request):
    teachers=Staff.objects.all()
    return render(request,'HOD/view_teacher.html',{'teachers':teachers})

def editTeacher(request,id):
    teacher = Staff.objects.filter(id=id)
    return render(request,'HOD/edit_teacher.html',{'teachers':teacher})

def updateTeacher(request):
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher_id')
        profile = request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')   
        birth_date = request.POST.get('dob_teacher')
        mobile = request.POST.get('mobile')
        gender =request.POST.get('gender') 
        joining_date = request.POST.get('join_date')
        qualification = request.POST.get('qualification')
        experience=  request.POST.get('experience')
        address = request.POST.get('address')
        
        user = Customuser.objects.get(id = teacher_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != None and password != "":
            user.set_password(password)
        if profile != None and profile != "":
            user.profile_pic =profile
        user.save()
        teacher= Staff.objects.get(admin=teacher_id)
        teacher.staff_gender=gender
        teacher.staff_dob=birth_date
        teacher.staff_mobile_no=mobile
        teacher.staff_joining_date=joining_date
        teacher.staff_qualification=qualification
        teacher.staff_experience=experience
        teacher.staff_address=address
        teacher.save()
        messages.success(request,'Record Successfully Updated !')
        return redirect('viewTeacher')
    return render(request,'HOD/edit_teacher.html')

def deleteTeacher(request,id):
    teacher= Staff.objects.get(id=id)
    teacher.delete()
    return redirect('viewTeacher')


def addSubject(request):
    courses= Course.objects.all()
    staffs= Staff.objects.all()
    
    if request.method == 'POST':
        subject_name=request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        
        course=Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)
        subject =Subject(
            name= subject_name,
            course =course,
            staff = staff
        )
        subject.save()
        messages.success(request,'Subject Added Successfully')
        return redirect('addSubject')
    context ={
        'course':courses,
        'staff':staffs,
    }
    return render(request,'HOD/add_subject.html',context)

def viewSubject(request):
    subject =Subject.objects.all()
    return render(request,'HOD/view_subject.html',{'subjects':subject})

def editSubject(request,id):
    subject = Subject.objects.filter(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    context={
         'subjects':subject,
         'course':course,
         'staff' : staff
    }
    return render(request,'HOD/edit_Subject.html',context)

def updateSubject(request):
    if request.method == 'POST':
        subject_id= request.POST.get('subject_id')
        subject_name=request.POST.get('subject_name')
        course_id= request.POST.get('course_id')
        staff_id= request.POST.get('staff_id')
        course=Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)
        subject= Subject(
            id= subject_id,
            name= subject_name,
            course = course,
            staff = staff,
        )
        subject.save()
        messages.success(request,'Subject Succesfully Updated')
        return redirect('viewSubject')
        
    return render(request,'HOD/edit_subject.html')

def deleteSubject(request,id):
    subject= Subject.objects.get(id=id)
    subject.delete()
    messages.success(request,'Subject Succesfully Deleted')
    return redirect('viewSubject')


def addSession(request):
    if request.method == "POST":
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        session = Session(
            session_start = session_start,
            session_end = session_end
        )
        session.save()
        messages.success(request,'Session Added Successfully')
    return render(request,'HOD/add_session.html')

def viewSession(request):
    session = Session.objects.all()
    context ={
        'sessions':session
    }
    return render(request,'HOD/view_session.html',context)

def editSession(request,id):     
    session = Session.objects.filter(id=id) 
    return render (request,'HOD/edit_session.html',{'sessions':session})

def updateSession(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        session = Session(
            id = session_id,
            session_start = session_start,
            session_end = session_end
        )
        print(session)
        session.save()
        messages.success(request,'Session Updated Sucessfully')
        return redirect('viewSession')
    return render(request,'HOD/edit_session.html')

def deleteSession(request,id):
    session = Session.objects.get(id=id)
    session.delete()
    return redirect('viewSession')
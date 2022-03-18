from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import *


def staffpage(request):
    return render(request,'Staff/home.html')

def staffnotification(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        notification = StaffNotification.objects.filter(staff_id =staff_id)
        context={
            'notification' : notification 
        }
    return render(request,'Staff/notification.html',context)

def staffnotifydone(request,id):
    notification = StaffNotification.objects.get(id =id)
    notification.message_status = 1
    notification.save()
    return redirect('notification')

def staffapplyleave(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        staff_leave_history = StaffLeave.objects.filter(staff_id = staff_id)
        context ={
            'staff_leave_history':staff_leave_history
        }
    return render(request,'Staff/apply_leave.html',context)

def staffsendleave(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('reason')
        staff= Staff.objects.get(admin = request.user.id)
        leave = StaffLeave(
            staff_id = staff,
            date = leave_date,
            text = leave_message
        )
        leave.save()
        messages.success(request,'Application Send Sucessfully')
    return render(request,'Staff/apply_leave.html')

def stafffeedbacks(request):
    id = Staff.objects.get(admin= request.user.id)
    feedbacks = StaffFeedback.objects.filter(staff_id = id )
    context ={
        'feedbacks':feedbacks
    }
    return render(request,'Staff/send_feedback.html',context)

def staffsavefeedbacks(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        staff = Staff.objects.get(admin = request.user.id)
        feedbacks = StaffFeedback(
            staff_id = staff,
            feedback =feedback
        )
        feedbacks.save()
        messages.success(request,'Feedback Send Sucessfully')
    return redirect('stafffeedback')

def stafftakeattendance(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(staff=staff_id)
    session_year = Session.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session_year = None
    students = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_id = request.POST.get('session_year_id')
            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = Session.objects.get(id=session_id)
            subjects = Subject.objects.filter(id= subject_id)
            for i in subjects:
                student_id = i.course.id
                students = Student.objects.filter(course_id = student_id)
    context ={
        'subjects':subjects,
        'session_year' :session_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action,
        'students':students
        
    }
    return render(request,'Staff/take_attendance.html',context)

def staffsaveattendance(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.get('student_id')
        get_subject = Subject.objects.get(id = subject_id)
        get_session_year = Session.objects.get(id=session_year_id)
        attendance = Attendance(
            subject_id  = get_subject,
            attendance_date = attendance_date,
            session_year = get_session_year
        )
        attendance.save()
        for i in student_id:
            stud_id = i
            st = int(stud_id)
            studs_id = Student.objects.get(id = st)
            report = AttendanceReport(
                student_id= studs_id,
                attendance_id =attendance
            )
            report.save()
            messages.success(request,'Attendance Taken')
    return redirect('takeattendance')

def staffviewattendance(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    subject = Subject.objects.filter(staff_id = staff_id)
    session_year = Session.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session_year = None
    attendance_date = None
    report= None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')
            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session.objects.get(id = session_year_id)
            attendance = Attendance.objects.filter(subject_id = get_subject,attendance_date =attendance_date)
            for i in attendance:
                attendance_id = i.id
                report = AttendanceReport.objects.filter(attendance_id = attendance_id)
            
    context ={
        'subjects':subject,
        'sessions':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'attendance_date':attendance_date,
        'reports':report
    }
    return render(request,'Staff/view_attendance.html',context)
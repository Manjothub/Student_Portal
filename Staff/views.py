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
    if action is not None:
        if request.method == 'POST':
            subject = request.POST.get('subject_id')
            session = request.POST.get('session_year_id')
            get_subject = Subject.objects.get(id = subject)
            get_session_year = Session.objects.get(id=session)
            subjects = Subject.objects.filter(id= subject)
    context ={
        'subjects':subjects,
        'session_year' :session_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action
        
    }
    return render(request,'Staff/take_attendance.html',context)
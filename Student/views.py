from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app .models import *

def studenthome(request):
    return render(request,'Student/home.html')

def studentnotification(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student = i.id
        notification = StudentNotification.objects.filter(student_id = student)
    context={
        'notification':notification
    }
    return render(request,'Student/notification.html',context)

def studentnotifydone(request,id):
    notification = StudentNotification.objects.get(id =id)
    notification.message_status = 1
    notification.save()
    return redirect('studentnotification')

def studentfeedback(request):
    id = Student.objects.get(admin= request.user.id)
    feedbacks = StudentFeedback.objects.filter(stud_id = id)
    context ={
        'feedbacks':feedbacks
    }
    return render(request,'Student/send_feedback.html',context)

def studentsavefeedback(request):
    if request.method == 'POST':
        student = Student.objects.get(admin = request.user.id)
        msg = request.POST.get('feedback')
        feedback = StudentFeedback(
            stud_id = student,
            text=msg
        )
        feedback.save()
        messages.success(request,'Feedback Send Sucessfully')
    return redirect('studentfeedbacks')

def studentleaveview(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student = i.id
        leaves = StudentLeave.objects.filter(student_id = student)
        context={
        'leaves':leaves
        }
    return render(request,'Student/apply_leave.html',context)

def studentsendleave(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('reason')
        student= Student.objects.get(admin = request.user.id)
        leave = StudentLeave(
            student_id = student,
            date = leave_date,
            text = leave_message
        )
        leave.save()
        messages.success(request,'Application Send Sucessfully')
    return redirect('studentleaveview')
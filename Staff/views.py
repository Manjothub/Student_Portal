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
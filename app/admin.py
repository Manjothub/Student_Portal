from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

@admin.register(Customuser)
class UserModel(UserAdmin):
    list_display=['username','user_type']

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Session)
admin.site.register(StaffNotification)
admin.site.register(StaffLeave)
admin.site.register(StaffFeedback)
admin.site.register(StudentNotification)
admin.site.register(StudentFeedback)
admin.site.register(StudentLeave)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)


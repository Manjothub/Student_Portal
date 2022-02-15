from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

@admin.register(Customuser)
class UserModel(UserAdmin):
    list_display=['username','user_type']

admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)


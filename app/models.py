from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


class Customuser(AbstractUser):
    USER ={
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT'),
    }
    user_type = models.CharField(choices=USER,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='uploads/profile_pic/')
    
    
class Course(models.Model):
    name= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Session(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)
    
    def __str__(self):
        return self.session_start + " TO " + self.session_end


class Student(models.Model):
    admin = models.OneToOneField(Customuser,on_delete = models.CASCADE)
    student_dob =models.DateField(auto_now_add=False)
    permanent_address = models.TextField(null=True)
    present_address =models.TextField(blank=True)
    gender = models.CharField(max_length=10)
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING,null=True)
    session_id =models.ForeignKey(Session,on_delete =models.DO_NOTHING,null=True)
    student_mobile_no =models.CharField(blank=False,max_length=10)
    student_optional_mobile_no =models.CharField(blank=True,max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name    

class Staff(models.Model):
    admin = models.OneToOneField(Customuser,on_delete = models.CASCADE)
    staff_gender = models.CharField(max_length=10)
    staff_dob = models.DateField(auto_now_add=False)
    staff_mobile_no = models.CharField(blank=False,max_length=10)
    staff_joining_date = models.DateField(auto_now_add=True)
    staff_qualification = models.CharField(max_length=100)
    staff_experience = models.CharField(max_length=10)
    staff_address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.admin.username

class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

    
class StaffNotification(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    message_status = models.IntegerField(null=True, default=0)
    
    def __str__(self):
        return self.staff_id.admin.first_name     
    
class StaffLeave(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    text = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name

class StaffFeedback(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete = models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name
    
class StudentNotification(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    message_status = models.IntegerField(null=True, default=0)
    
    def __str__(self):
        return self.student_id.admin.first_name     
    
class StudentFeedback(models.Model):
    stud_id = models.ForeignKey(Student,on_delete = models.CASCADE)
    text = models.TextField()
    text_reply = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.stud_id.admin.first_name + self.stud_id.admin.last_name


class StudentLeave(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    text = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.student_id.admin.first_name + self.student_id.admin.last_name
    
    
class Attendance(models.Model):
    subject_id = models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    session_year = models.ForeignKey(Session,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject_id.name 

class AttendanceReport(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.student_id.admin.first_name + self.student_id.admin.last_name
    
class StudentResult(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    assignment_mark = models.IntegerField()
    exam_mark = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.student_id.admin.first_name
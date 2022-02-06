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
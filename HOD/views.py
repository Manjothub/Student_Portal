from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def hodpage(request):
    return render(request,'HOD/home.html')

from django.shortcuts import render
from django.http import HttpResponse
from .models import student
# Create your views here.

def index(request):
    return render(request,'index.html')

def contactus(request):
    return HttpResponse("Contact us here!")

def student_by_rollno(request, rollno):
    stu = student.objects.get(pk=rollno)
    return render(request,'studentdetails.html',{'student':stu})


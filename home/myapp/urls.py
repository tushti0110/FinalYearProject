from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('contactus/',views.contactus,name = 'contactus'),
    path('student/<int:rollno>',views.student_by_rollno,name = 'student_by_rollno'),
]
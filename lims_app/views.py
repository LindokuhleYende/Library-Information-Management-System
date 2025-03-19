from django.shortcuts import render, redirect
from django.contrib import admin
from django.http import HttpResponse

#Register your models here


# Create your views here.
def home(request):
    return render(request, "home.html", context={"current_tab:": "home"})

def shopping(request):
    return HttpResponse("Welcome to shopping")

def save_student(request):
    student_name = request.POST["student_name"]
    return render(request, "welcome.html",context={"student_name":student_name})
from django.shortcuts import render, redirect
from django.contrib import admin
from django.http import HttpResponse
from .models import *

#Register your models here


# Create your views here.
def home(request):
    return render(request, "home.html", context={"current_tab:": "home"})

def readers(request):
    return render(request, "readers.html", context={"current_tab:": "readers"})

def shopping(request):
    return HttpResponse("Welcome to shopping")

def save_student(request):
    student_name = request.POST["student_name"]
    return render(request, "welcome.html",context={"student_name":student_name})

def readers_tab(request):
    readers= reader.objects.all()
    return render(request, "readers.html", context={"current_tab:": "readers", "readers":readers})
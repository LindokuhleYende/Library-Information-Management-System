from django.shortcuts import render, redirect
from django.contrib import admin
from django.http import HttpResponse
from .models import *

#Register your models here


# Create your views here.
def home(request):
    return render(request, "home.html", context={"current_tab:": "home"})

##def readers(request):
    #return render(request, "readers.html", context={"current_tab:": "readers"})

def shopping(request):
    return HttpResponse("Welcome to shopping")

def save_student(request):
    student_name = request.POST["student_name"]
    return render(request, "welcome.html",context={"student_name":student_name})

def readers_tab(request):
    readers= reader.objects.all()
    return render(request, "readers.html", context={"current_tab:": "readers", "readers":readers})

def save_reader(request):
    reader_item = reader(reference_id=request.POST["reference_id"],
                         reader_name=request.POST["reader_name"],
                         reader_contact=request.POST["reader_contact"],
                         reader_address=request.POST["reader_address"],
                         active =  True
                         )
    reader_item.save()
    return redirect("/readers")
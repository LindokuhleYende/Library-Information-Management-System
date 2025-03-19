from django.shortcuts import render, redirect
from django.contrib import admin
from django.http import HttpResponse

#Register your models here


# Create your views here.
def home(request):
    return HttpResponse("Hello world")

def shopping(request):
    return HttpResponse("Welcome to shopping")

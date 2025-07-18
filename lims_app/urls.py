"""
URL configuration for lims_portal project.

The `urlpatterns` list routes URLs to views. For more information please see
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #path("readers_tab",readers_tab),
    path("readers",readers_tab),
    path("/",home),
    path("home", home),
    path("readers/add", save_reader),
    path('books/', book_list, name='book_list'),
    path('add-book/', add_book, name='add_book'),
    path('decrease-quantity/<int:book_id>/', decrease_quantity, name='decrease_quantity')

]

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import admin, messages
from django.http import HttpResponse
from .models import *

#Register your models here


# Create your views here.
def home(request):
    return render(request, "home.html", context={"current_tab:": "home"})

##def readers(request):
    #return render(request, "readers.html", context={"current_tab:": "readers"})

# def shopping(request):
    # return HttpResponse("Welcome to shopping")

# def save_student(request):
    # student_name = request.POST["student_name"]
    # return render(request, "welcome.html",context={"student_name":student_name})

def readers_tab(request):
    if request.method=="GET":
        readers= reader.objects.all()
        return render(request, "readers.html", context={"current_tab:": "readers", "readers":readers})
    else:
        query = request.POST["query"]
        readers = reader.objects.raw("select * from lims_app_reader where reader_name like '%"+query+"%'")
        return render(request, "readers.html", context={"current_tab:": "readers", "readers":readers, "query":query})

def save_reader(request):
    reader_item = reader(reference_id=request.POST["reference_id"],
                         reader_name=request.POST["reader_name"],
                         reader_contact=request.POST["reader_contact"],
                         reader_address=request.POST["reader_address"],
                         active =  True
                         )
    reader_item.save()
    return redirect("/readers")

def book_list(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        publication_date = request.POST['publication_date']
        quantity = request.POST['quantity']

        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            publication_date=publication_date,
            quantity=quantity
        )
        return redirect('book_list')
    return render(request, 'add_book.html')

def decrease_quantity(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.quantity > 0:
        book.quantity -= 1
        book.save()
        messages.success(request, f'Quantity of "{book.title}" decreased by 1.')
    else:
        messages.warning(request, f'Cannot decrease quantity. "{book.title}" is out of stock.')
    return redirect('book_list')
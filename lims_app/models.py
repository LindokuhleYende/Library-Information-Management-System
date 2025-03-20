from django.db import models

# Create your models here.
class reader(models.Model):
    def __str__(self):
        return self.reader_name
    reference_id = models.CharField(max_length=200)
    reader_name = models.CharField(max_length=200)
    reader_contact = models.CharField(max_length=200)
    reader_address = models.TextField()
    active = models.BooleanField(default=True)

class Book(models.Model):
     title = models.CharField(max_length=200)
     author = models.CharField(max_length=100)
     isbn = models.CharField(max_length=13, unique=True)
     publication_date = models.DateField()
     quantity = models.PositiveIntegerField()
     
     def __str__(self):
         return self.title
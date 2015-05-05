from django.contrib import admin

# Register your models here.
from .models import Book, Comment, BookPage


admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(BookPage)

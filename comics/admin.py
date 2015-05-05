from django.contrib import admin

# Register your models here.
from .models import Book, BookPage, Comment


admin.site.register(Book)
admin.site.register(BookPage)
admin.site.register(Comment)


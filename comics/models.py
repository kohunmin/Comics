from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date added')
    
    def __str__(self):
    	return self.title


class BookPage(models.Model):

    book_id = models.ForeignKey(Book)
    pic_url = models.CharField(max_length=300)

    def __str__(self):
    	return self.pic_url

class Comment(models.Model):
    book_page_id = models.ForeignKey(BookPage)
    body = models.TextField(max_length=100)

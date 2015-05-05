from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date added')
    
    def __str__(self):
    	return self.title  + " : " + str(self.pk)

class BookPage(models.Model):
	book = models.ForeignKey(Book)
	page = models.IntegerField(default=0)
	pic = models.CharField(max_length=1000)

	def __str__(self):
		return str(self.page)

class Comment(models.Model):
	bookpage = models.ForeignKey(BookPage)
	comment = models.CharField(max_length=200)
	date = models.DateTimeField('time added')

	def __str__(self):
		return self.comment
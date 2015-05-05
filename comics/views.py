
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render

from .models import Book, BookPage


# Create your views here.
def home(request):
	# collect every info from Book db
	book_list = Book.objects.order_by('-pub_date')

	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'book_list': book_list,
		})


	# call index.html
	return HttpResponse(template.render(context))

def page(request, book_id):
	try:
		bookpage = BookPage.objects.get(pk=book_id,page=1)
	except BookPage.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'page.html' , {'bookpagePic':bookpage.pic})
	

def pageDetail(request, book_id, bookpage_id):
	try:
		bookpage = BookPage.objects.get(pk=book_id,page=1)
	except BookPage.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'page.html' , {'bookpagePic':bookpage.pic})
	r#eturn HttpResponse(str(book_id) + "," + str(bookpage_id))
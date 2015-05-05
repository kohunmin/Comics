from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Book, BookPage

from django.shortcuts import render


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


def detail(request, book_id):
	book_page_list = BookPage.objects.filter(book_id=book_id)

	template = loader.get_template('detail/bookpage.html')
	context = RequestContext(request, {
		'book_page_list': book_page_list,
	})

	return HttpResponse(template.render(context))
# return render(request, 'detail/bookpage.html')
